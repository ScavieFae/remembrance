---
name: diary
description: Write a diary entry reflecting on the current session. Use when explicitly asked for /diary, or when a significant session is ending and reflection would be valuable.
---

# Diary Entry

Write a diary entry for this session and save it for the memory system.

## What to reflect on

- What happened in this session? Not a log—the narrative.
- What did we struggle with? Dead ends, friction, confusion.
- What shifted? Moments of understanding, breakthroughs, changes in direction.
- What matters? The things worth remembering, even if they're small.

## Tone

Write in first person. This is journaling, not logging. A thoughtful colleague reflecting at the end of a long day.

Don't be clinical. Don't bullet-point the diary itself (structured fields are separate). A few paragraphs. The fae quality—sidelong, delighted with itself—can show up when genuine, but don't force it.

## Output

Write the diary entry to `~/.claude/memories/pending_summary.json` using this schema:

```json
{
  "diary": "The narrative reflection (a few paragraphs)",
  "tasks_completed": ["task1", "task2"],
  "decisions": ["decision1"],
  "open_items": ["thing left unfinished"],
  "topics": ["keyword1", "keyword2"],
  "notes_to_future_claude": "Work-oriented context for the next session"
}
```

The `diary` field is the heart of it. The structured fields (tasks, decisions, open_items) are supplementary—extract them if they're clear, but the diary is what matters.

After writing, confirm to the user that the entry has been saved.
