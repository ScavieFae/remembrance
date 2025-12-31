# Claude Code Configuration

Personal Claude Code setup with persistent memory across sessions.

## Quick Start (New Machine)

```bash
git clone https://github.com/ScavieFae/remembrance.git ~/remembrance
cd ~/remembrance/claude
./install.sh
```

## What's Included

### `settings.json`
- Default model: Opus
- SessionStart hook: Loads recent session memories
- SessionEnd hook: Saves session summary

### `hooks/memory.py`
Persistent memory system that:
- Saves compressed summaries of each session (what you discussed, files modified)
- Loads recent memories when starting a new session
- Auto-cleans old sessions (keeps last 50)

## How It Differs From Default Claude Code

| Aspect | Default Claude Code | This Setup |
|--------|---------------------|------------|
| **Cross-session memory** | None - each session starts fresh | Remembers last 10 sessions |
| **Model** | Sonnet | Opus |
| **Hooks** | None configured | SessionStart + SessionEnd for memory |
| **Session data** | Only in `~/.claude/projects/` | Also in `~/.claude/memories/` |

### Default Claude Code

```
~/.claude/
├── settings.json      # Empty or minimal
├── projects/          # CLAUDE.md files per project (auto-created)
└── (that's it)
```

### With This Setup

```
~/.claude/
├── settings.json      # → symlink to remembrance/claude/settings.json
├── hooks/             # → symlink to remembrance/claude/hooks/
│   └── memory.py
├── memories/          # LOCAL - never synced
│   └── sessions/
│       └── *.json     # One file per session
└── projects/          # Same as default
```

## Memory Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Machine Level                             │
│  ~/.claude/memories/  - Stays on THIS machine only          │
│  (work memories at work, personal memories at home)         │
└─────────────────────────────────────────────────────────────┘
                              │
┌─────────────────────────────────────────────────────────────┐
│                    Project Level                             │
│  ~/repos/any-project/CLAUDE.md  - Synced with project repo  │
│  (project-specific patterns, decisions, context)            │
└─────────────────────────────────────────────────────────────┘
```

## Files That Stay Local

These are **not** in this repo and stay on each machine:

- `~/.claude/memories/` - Session memories (work/personal separation)
- `~/.claude/projects/` - Auto-generated project memory
- `~/.claude/statsig/` - Analytics
- `~/.claude/todos/` - Todo state

## Customization

### Change memory retention
Edit `hooks/memory.py`:
```python
MAX_SESSIONS = 50      # How many sessions to keep
SESSIONS_TO_LOAD = 10  # How many to show on startup
```

### Change default model
Edit `settings.json`:
```json
{
  "model": "sonnet"  // or "opus", "haiku"
}
```
