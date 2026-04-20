#!/usr/bin/env python3
"""PreCompact hook — append compaction event to ~/.claude/metrics/compactions.jsonl.

Reads Claude Code PreCompact hook JSON from stdin, writes one line per event.
Fails silent so compaction is never blocked.
"""
import json
import sys
from datetime import datetime, timezone
from pathlib import Path


def main() -> int:
    try:
        data = json.load(sys.stdin)
    except Exception:
        return 0  # don't block compaction if input is unreadable

    metrics_dir = Path.home() / ".claude" / "metrics"
    metrics_dir.mkdir(parents=True, exist_ok=True)
    out = metrics_dir / "compactions.jsonl"

    event = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "session_id": data.get("session_id"),
        "cwd": data.get("cwd"),
        "trigger": data.get("trigger"),
        "transcript_path": data.get("transcript_path"),
    }

    try:
        with out.open("a") as f:
            f.write(json.dumps(event) + "\n")
    except Exception:
        return 0  # never block compaction on a write error

    return 0


if __name__ == "__main__":
    sys.exit(main())
