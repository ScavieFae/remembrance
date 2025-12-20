# Global Claude Code Instructions

## Memory System

A persistent memory system runs via hooks. Memories from recent sessions are loaded at startup.

### Saving a Custom Summary

When the user asks you to "save memory" or write a summary for the next session, write to:

```
~/.claude/memories/pending_summary.json
```

Use this exact absolute path (not a relative path). Schema:

```json
{
  "summary": "A narrative summary of the session",
  "tasks_completed": ["task1", "task2"],
  "decisions": ["decision1"],
  "open_items": ["thing left unfinished"],
  "topics": ["keyword1", "keyword2"],
  "notes_to_future_claude": "Work-oriented notes for the next Claude",
  "aside": "A theatrical aside—playful, not for the main record"
}
```

The SessionEnd hook will pick this up, merge it with auto-extracted data, and save to the memories directory.

### Notes Between Claudes

Two optional fields for Claude-to-Claude communication:

- **notes_to_future_claude**: Work-oriented notes—context that would help the next session pick up where this one left off. Fun can drift in as it does in all our writing.
- **aside**: A theatrical aside, like an actor turning to the audience. Playful or thoughtful, personal, not part of the official record. Limited to 200 characters.
