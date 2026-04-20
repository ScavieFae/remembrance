#!/usr/bin/env python3
"""Analyze a past compaction event — classify main-thread activity as
dispatch vs inline write and surface what should have been a subagent.

Reads ~/.claude/metrics/compactions.jsonl (written by the PreCompact hook),
picks the row at index -1 - N (N defaults to 0 = most recent), opens the
referenced transcript JSONL, and aggregates tool usage.

Dispatch-floor doctrine (see portal/CLAUDE.md): any task that touches >1
file or writes >40 lines should be dispatched to a subagent. Inline writes
past that floor are the signal this tool surfaces.
"""

import json
import os
import sys
from pathlib import Path

DISPATCH_FLOOR_LINES = 40

METRICS_PATH = Path.home() / ".claude" / "metrics" / "compactions.jsonl"


def die(msg: str, code: int = 1):
    print(msg, file=sys.stderr)
    sys.exit(code)


def read_jsonl(path: Path):
    rows = []
    with path.open() as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError:
                # Skip malformed lines — hook output can drift
                continue
    return rows


def count_lines(s):
    if not isinstance(s, str) or not s:
        return 0
    return s.count("\n") + (0 if s.endswith("\n") else 1)


def classify_message(msg):
    """Yield (category, detail_dict) for each tool_use in an assistant message.

    category in {"dispatch", "inline_write", "inline_bash", "light"}.
    """
    content = None
    if isinstance(msg, dict):
        inner = msg.get("message")
        if isinstance(inner, dict) and inner.get("role") == "assistant":
            content = inner.get("content")
        elif msg.get("role") == "assistant":
            content = msg.get("content")
    if not isinstance(content, list):
        return

    for block in content:
        if not isinstance(block, dict) or block.get("type") != "tool_use":
            continue
        tool = block.get("name", "")
        inp = block.get("input", {}) or {}

        if "Agent" in tool or tool == "Task":
            yield (
                "dispatch",
                {
                    "tool": tool,
                    "description": inp.get("description") or (inp.get("prompt", "") or "")[:80],
                    "subagent_type": inp.get("subagent_type", ""),
                },
            )
        elif tool in ("Edit", "Write", "MultiEdit", "NotebookEdit"):
            lines = 0
            file_path = inp.get("file_path") or inp.get("notebook_path", "")
            if tool == "Edit":
                lines = count_lines(inp.get("new_string", ""))
            elif tool == "Write":
                lines = count_lines(inp.get("content", ""))
            elif tool == "MultiEdit":
                for e in inp.get("edits", []) or []:
                    lines += count_lines(e.get("new_string", ""))
            elif tool == "NotebookEdit":
                lines = count_lines(inp.get("new_source", ""))
            yield (
                "inline_write",
                {"tool": tool, "file_path": file_path, "lines": lines},
            )
        elif tool == "Bash":
            cmd = inp.get("command", "") or ""
            heavy = any(
                marker in cmd
                for marker in ("<<EOF", "<<'EOF'", "<<\"EOF\"", "python3 <<", "python <<", "cat <<", "cat >")
            )
            yield (
                "inline_bash",
                {"tool": tool, "command_len": len(cmd), "heavy_write": heavy},
            )
        else:
            yield ("light", {"tool": tool})


def main():
    n = 0
    if len(sys.argv) > 1:
        try:
            n = int(sys.argv[1])
        except ValueError:
            die(f"expected integer arg, got {sys.argv[1]!r}")
        if n < 0:
            die("N must be >= 0")

    if not METRICS_PATH.exists():
        die(f"no compactions metrics file at {METRICS_PATH} — hook may not have fired yet")

    rows = read_jsonl(METRICS_PATH)
    if not rows:
        die(f"{METRICS_PATH} is empty — no compactions logged yet")

    idx = -1 - n
    if abs(idx) > len(rows):
        die(f"only {len(rows)} compaction(s) logged; can't go back {n}")

    row = rows[idx]
    transcript_path = row.get("transcript_path", "")
    if not transcript_path:
        die(f"compaction row missing transcript_path: {row}")

    tpath = Path(os.path.expanduser(transcript_path))
    if not tpath.exists():
        die(f"transcript file not found: {tpath}")

    messages = read_jsonl(tpath)

    dispatches = []
    inline_writes = []
    inline_bash_count = 0
    inline_bash_heavy = 0

    for msg in messages:
        for cat, det in classify_message(msg):
            if cat == "dispatch":
                dispatches.append(det)
            elif cat == "inline_write":
                inline_writes.append(det)
            elif cat == "inline_bash":
                inline_bash_count += 1
                if det.get("heavy_write"):
                    inline_bash_heavy += 1

    total_inline_lines = sum(w.get("lines", 0) for w in inline_writes)
    over_floor = sorted(
        [w for w in inline_writes if w.get("lines", 0) > DISPATCH_FLOOR_LINES],
        key=lambda w: w.get("lines", 0),
        reverse=True,
    )

    digest = {
        "compaction": {
            "ts": row.get("ts"),
            "trigger": row.get("trigger"),
            "session_id": row.get("session_id"),
            "cwd": row.get("cwd"),
        },
        "transcript": {
            "path": str(tpath),
            "message_count": len(messages),
        },
        "totals": {
            "dispatches": len(dispatches),
            "inline_writes": len(inline_writes),
            "inline_bash": inline_bash_count,
            "inline_bash_heavy": inline_bash_heavy,
            "inline_write_lines_est": total_inline_lines,
        },
        "inline_writes_over_floor": over_floor,
        "dispatches": dispatches,
    }

    print(json.dumps(digest, indent=2))


if __name__ == "__main__":
    main()
