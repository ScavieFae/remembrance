---
name: postmortem
description: Post-mortem a context compaction — surface which main-thread tasks should have been subagents. Use when the user asks for /postmortem, or when reviewing why a session compacted.
---

# /postmortem — Dispatch-Floor Post-Mortem

Post-mortem the most recent (or an older) context compaction. Surface which main-thread writes should have been dispatched to subagents.

Data source: `~/.claude/metrics/compactions.jsonl` (written by the `PreCompact` hook). Each row references the transcript that led up to the compaction.

Dispatch-floor doctrine: any task that touches more than one file or produces more than 40 lines should be dispatched to a subagent. Compaction is the failure signal.

## Step 1: Run the analyzer

```bash
python3 ~/.claude/skills/postmortem/analyze.py
```

Optional integer arg: how many compactions back. `0` (default) = most recent. `1` = second-most-recent. Etc.

```bash
python3 ~/.claude/skills/postmortem/analyze.py 2   # three compactions ago
```

The script prints a JSON digest to stdout. If the metrics file is missing or empty, it prints a friendly message to stderr and exits 1 — report that to the user and stop.

## Step 2: Read the digest

The digest shape:

```json
{
  "compaction": { "ts": "...", "trigger": "auto|manual", "session_id": "...", "cwd": "..." },
  "transcript": { "path": "...", "message_count": N },
  "totals": {
    "dispatches": 5,
    "inline_writes": 12,
    "inline_bash": 3,
    "inline_bash_heavy": 1,
    "inline_write_lines_est": 487
  },
  "inline_writes_over_floor": [ { "tool": "Write", "file_path": "...", "lines": 62 }, ... ],
  "dispatches": [ { "description": "...", "subagent_type": "..." }, ... ]
}
```

## Step 3: Write the post-mortem

150 words or less. Deliver the signal, stop.

Include:
- **When** the compaction fired (ts), **message count** for the session, **trigger** (auto vs manual).
- **Dispatch ratio**: X inline writes vs Y dispatches.
- **Top 3 inline writes over the 40-line floor**, by file path and line count.
- **One concrete suggestion** for next session — something specific the transcript shows (e.g., "dispatch wiki-page rewrites next time", "batch the Edit storm on `foo.rs` into a coder brief").

Don't moralize. Don't explain the doctrine. Don't pad. Assume the reader knows what dispatching is — this is diagnostic output, not a lecture.

## Notes

- If `totals.dispatches` is already high and `inline_writes_over_floor` is short, say so — "dispatch discipline was solid, the compaction came from volume not structure." Don't manufacture failure.
- If the transcript can't be read, the script exits 1 — surface that error to the user verbatim, don't silently continue.
