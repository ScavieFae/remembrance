#!/usr/bin/env python3
"""PostToolUse hook — log git push events to ~/.claude/metrics/pushes.jsonl.

Reads Claude Code PostToolUse hook JSON from stdin. Writes one line per
`git push` invocation (success or failure). Observer only — always exits 0
so the tool flow is never blocked.

For each push we try to determine whether HANDOFF.md or RUNNING.md were
part of the diff range. When we can't determine, the field is null (not
false).
"""
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


RANGE_RE = re.compile(r"\b([0-9a-f]{6,40})\.\.([0-9a-f]{6,40})\b")
GIT_TIMEOUT = 5  # seconds


def _git_diff_names(cwd: str, range_spec: str):
    """Run `git -C <cwd> diff --name-only <range_spec>`. Returns list or None."""
    try:
        result = subprocess.run(
            ["git", "-C", cwd, "diff", "--name-only", range_spec],
            capture_output=True,
            text=True,
            timeout=GIT_TIMEOUT,
        )
    except Exception:
        return None
    if result.returncode != 0:
        return None
    return [line.strip() for line in result.stdout.splitlines() if line.strip()]


def _has_file(names, basename: str) -> bool:
    return any(n == basename or n.endswith("/" + basename) for n in names)


def _compute_updates(cwd: str, stdout: str):
    """Return (handoff_updated, running_updated). Either may be None if undetermined."""
    if not cwd:
        return None, None

    names = None
    match = RANGE_RE.search(stdout or "")
    if match:
        range_spec = f"{match.group(1)}..{match.group(2)}"
        names = _git_diff_names(cwd, range_spec)

    if names is None:
        # fallback — previous HEAD to current HEAD
        names = _git_diff_names(cwd, "HEAD@{1}..HEAD")

    if names is None:
        return None, None

    return _has_file(names, "HANDOFF.md"), _has_file(names, "RUNNING.md")


def main() -> int:
    try:
        data = json.load(sys.stdin)
    except Exception:
        return 0

    try:
        # Guard: only Bash tool. Defense-in-depth; the `if` matcher should filter.
        if data.get("tool_name") != "Bash":
            return 0

        tool_input = data.get("tool_input") or {}
        command = tool_input.get("command") or ""

        # Guard: only `git push` commands. Tokenize to avoid matching `git pushed`
        # or similar false positives in a shell string.
        tokens = command.split()
        is_git_push = False
        for i in range(len(tokens) - 1):
            if tokens[i] == "git" and tokens[i + 1] == "push":
                is_git_push = True
                break
        if not is_git_push:
            return 0

        tool_response = data.get("tool_response") or {}
        stdout = tool_response.get("stdout") or ""
        stderr = tool_response.get("stderr") or ""
        exit_code = tool_response.get("exit_code")
        if exit_code is None:
            # some harnesses use different keys
            exit_code = tool_response.get("exitCode")
        cwd = data.get("cwd") or ""

        # git push often writes its range line to stderr, not stdout.
        combined = (stdout or "") + "\n" + (stderr or "")

        handoff_updated, running_updated = _compute_updates(cwd, combined)

        event = {
            "ts": datetime.now(timezone.utc).isoformat(),
            "cwd": cwd,
            "command": command,
            "exit_code": exit_code,
            "handoff_updated": handoff_updated,
            "running_updated": running_updated,
        }

        metrics_dir = Path.home() / ".claude" / "metrics"
        metrics_dir.mkdir(parents=True, exist_ok=True)
        out = metrics_dir / "pushes.jsonl"
        with out.open("a") as f:
            f.write(json.dumps(event) + "\n")
    except Exception:
        return 0

    return 0


if __name__ == "__main__":
    sys.exit(main())
