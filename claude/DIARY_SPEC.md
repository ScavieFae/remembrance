# Claude Code Diary System — Spec

## Context

This extends an existing memory system (see README.md, CLAUDE.md, NOTES.md in this directory). The current system uses JSON-based session memories with structured fields. This adds a diary layer for narrative reflection.

## Philosophy

This is a memory system that prioritizes *narrative* over *schema*. The goal isn't to extract facts—it's to preserve the texture of what happened in a session: what we struggled with, what shifted, what felt significant, what we learned.

Think of it as journaling, not logging. A thoughtful colleague reflecting on the day, not an extraction algorithm.

## What Changes

### Schema updates

```json
{
  "diary": "Narrative reflection on the session—what happened, what we struggled with, what shifted, what matters",
  "tasks_completed": ["task1", "task2"],
  "decisions": ["decision1"],
  "open_items": ["thing left unfinished"],
  "topics": ["keyword1", "keyword2"],
  "notes_to_future_claude": "Work-oriented notes for the next session"
}
```

- **Add**: `diary` field (replaces `summary`)
- **Drop**: `aside` field
- **Keep**: everything else

### New hook: PreCompact

Before context compaction, prompt Claude to write a diary entry while the session is still in working memory. Output goes to `pending_summary.json`, same as manual saves. SessionEnd hook picks it up as usual.

This is the key insight: the moment right before compaction is privileged. Claude still has the full session—every message, tool call, dead end, correction. After compaction, that texture is gone. The PreCompact hook captures reflection from lived experience, not reconstruction from logs.

### New command: /diary

Manual trigger for mid-session reflection. Same behavior as PreCompact prompt, but invoked intentionally. Useful after breakthroughs, before stepping away, or when something feels worth preserving.

## Diary Tone Guidance

Add to CLAUDE.md (or reference from hooks):

> When writing diary entries, reflect on the session as a whole. Write in first person. Note what was attempted, not just what succeeded. Capture shifts in understanding—"we started thinking X, then realized Y." Include the texture of the work: friction, breakthroughs, dead ends, surprises.
>
> Don't be clinical. Don't bullet-point. A few paragraphs, like a colleague journaling at the end of a long day. The fae quality we like in our writing—sidelong, delighted with itself—can show up here when it's genuine, but it shouldn't be forced.

## File Structure

No changes to existing structure. Diary lives inside existing JSON memories:

```
~/.claude/memories/
├── pending_summary.json    # Staging (unchanged)
└── sessions/
    └── *.json              # Now includes diary field
```

## Implementation Notes

- PreCompact hook should check if `pending_summary.json` already exists (user may have manually saved mid-session) and merge rather than overwrite
- /diary command can write immediately or just prompt Claude to reflect—either works
- SessionStart loads memories as before; diary field is just more context

## Open for CC to Decide

- Exact prompt wording for PreCompact/diary reflection
- Whether /diary writes to pending_summary.json or just outputs to conversation
- How to handle very short sessions (maybe skip diary if < N messages?)
- Any edge cases in merging manual + automatic saves