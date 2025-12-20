# Memory System Notes

## Saving memories

When user asks to "save memory", write summary to:
```
~/.claude/memories/pending_summary.json
```

NOT to the current working directory. The SessionEnd hook looks for it at that specific path.

## Schema
```json
{
  "summary": "Narrative description of the session",
  "tasks_completed": ["task1", "task2"],
  "decisions": ["decision1", "decision2"],
  "open_items": ["item1"],
  "topics": ["topic1", "topic2"],
  "notes_to_future_claude": "Work context for the next session",
  "aside": "A theatrical aside (200 char limit)"
}
```

Note: `files_modified` is auto-extracted from the transcript—no need to include it.

## Claude-to-Claude Communication

Two optional fields for passing notes between sessions:

- **notes_to_future_claude**: Work-oriented context that helps the next session pick up where this one left off. Can be practical or playful—whatever would actually help.

- **aside**: A theatrical aside, like an actor turning to the audience. Personal, playful, not part of the official record. Limited to 200 characters. Use sparingly.
