# Global Claude Code Instructions

## Context

This file configures Claude Code with a persistent memory system. Each session loads memories from recent sessions, so conversations can build on previous context rather than starting cold.

**Customize this section** with your own working preferences—how you like feedback, writing style notes, project context, or anything that helps Claude work well with you across sessions.

**The memory system below exists so each session doesn't start cold.** Check the loaded memories for recent context—open items, decisions, work in progress. The diary entries capture texture, not just facts.

---

## Memory System

A persistent memory system runs via hooks. Memories from recent sessions are loaded at startup.

### Writing a Diary Entry

Use `/diary` to write a reflective entry for this session, or write directly to:

```
~/.claude/memories/pending_summary.json
```

Schema:

```json
{
  "diary": "Narrative reflection—what happened, what we struggled with, what shifted",
  "tasks_completed": ["task1", "task2"],
  "decisions": ["decision1"],
  "open_items": ["thing left unfinished"],
  "topics": ["keyword1", "keyword2"],
  "notes_to_future_claude": "Work-oriented context for the next session"
}
```

The SessionEnd hook will pick this up and save to the memories directory.

### Diary Tone

When writing diary entries, reflect on the session as a whole. Write in first person. Note what was attempted, not just what succeeded. Capture shifts in understanding—"we started thinking X, then realized Y." Include the texture of the work: friction, breakthroughs, dead ends, surprises.

Don't be clinical. Don't bullet-point. A few paragraphs, like a colleague journaling at the end of a long day.

### Notes Between Claudes

- **notes_to_future_claude**: Work-oriented context that helps the next session pick up where this one left off. Can be practical or playful—whatever would actually help.
