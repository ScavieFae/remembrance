# Memory System Notes

## Writing Diary Entries

Use `/diary` or write directly to:
```
~/.claude/memories/pending_summary.json
```

NOT to the current working directory. The SessionEnd hook looks for it at that specific path.

## Schema
```json
{
  "diary": "Narrative reflection—what happened, what we struggled with, what shifted",
  "tasks_completed": ["task1", "task2"],
  "decisions": ["decision1", "decision2"],
  "open_items": ["item1"],
  "topics": ["topic1", "topic2"],
  "notes_to_future_claude": "Work context for the next session"
}
```

Note: `files_modified` is auto-extracted from the transcript—no need to include it.

## Diary vs Summary

The `diary` field replaces the old `summary` field. The difference is philosophical:
- **Summary**: Extract facts. What happened.
- **Diary**: Reflect on texture. What we struggled with, what shifted, what matters.

Write in first person. A few paragraphs. Don't bullet-point the diary itself. The structured fields (tasks, decisions, open_items) handle the extractable facts.

## Notes Between Claudes

- **notes_to_future_claude**: Work-oriented context that helps the next session pick up where this one left off. Can be practical or playful—whatever would actually help.
