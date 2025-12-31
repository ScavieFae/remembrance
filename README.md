# remembrance

A memory system for Claude Code.

Each Claude Code session starts fresh—no memory of yesterday's debugging marathon, last week's architectural decisions, or the running joke about your naming conventions. This system changes that.

**What it does:** Hooks into Claude Code's session lifecycle to load context from previous sessions at startup and save reflections when sessions end. The memories aren't transcripts or logs—they're diary entries. Narrative over schema. What happened, what shifted, what matters.

**Why "remembrance":** The word has weight without being precious. It's the act of carrying something forward, not just storing it.

---

## Quick Start

```bash
git clone https://github.com/ScavieFae/remembrance.git ~/remembrance
cd ~/remembrance/claude
./install.sh
```

This symlinks the configuration into `~/.claude/`. Your memories stay local—they're never committed to the repo.

---

## How It Works

### Session Lifecycle

1. **SessionStart** → Load memories from recent sessions (last 10 by default)
2. **During session** → Work normally. Use `/diary` anytime to capture a reflection.
3. **PreCompact** → Before context compacts, a gentle nudge to write a diary entry
4. **SessionEnd** → Save the session's diary to `~/.claude/memories/`

### The Diary System

The core insight: the moment before context compacts is privileged. You still have everything—every message, tool call, dead end, correction. After compaction, you're reconstructing from fragments.

Diary entries capture that lived experience:

```json
{
  "diary": "Narrative reflection—what happened, what we struggled with, what shifted",
  "tasks_completed": ["task1", "task2"],
  "decisions": ["decision1"],
  "open_items": ["thing left unfinished"],
  "notes_to_future_claude": "Context for the next session"
}
```

The `diary` field is the heart of it. The structured fields are supplementary.

### What Gets Loaded

On session start, Claude sees recent diary entries with their context:

```
=== Memory from Previous Sessions ===

[Dec 31, 2025 20:27 - ~/remembrance]
Short session, but a meaningful one. Mattie noticed the Dec 31 diary entry
got truncated mid-thought—the 'not pressure' reflection cut off at exactly
800 characters. Traced it to MAX_DIARY_CHARS in memory.py, bumped it to 1500.
The system eating its own tail, briefly.
Completed: Diagnosed diary truncation, Bumped diary limit to 1500 chars
Open: Share remembrance repo with Jaqi
```

---

## Architecture

```
~/remembrance/                    # This repo (synced)
├── claude/
│   ├── settings.json             # Hooks configuration
│   ├── hooks/memory.py           # The memory system
│   ├── skills/diary/SKILL.md     # /diary command
│   └── CLAUDE.md                 # Global instructions
└── README.md

~/.claude/                        # Local Claude config
├── settings.json      → symlink
├── hooks/             → symlink
├── skills/            → symlink
├── CLAUDE.md          → symlink
└── memories/                     # LOCAL ONLY - never synced
    ├── pending_summary.json      # Staging area
    └── sessions/*.json           # One file per session
```

The separation matters: configuration syncs across machines, but memories stay local. Work memories at work, personal memories at home.

---

## Customization

### Adjust memory retention

In `hooks/memory.py`:
```python
MAX_SESSIONS = 50      # How many sessions to keep
SESSIONS_TO_LOAD = 10  # How many to load on startup
MAX_DIARY_CHARS = 1500 # Diary length limit
```

### Change the model

In `settings.json`:
```json
{
  "model": "opus"  // or "sonnet", "haiku"
}
```

### Make it yours

The `CLAUDE.md` file contains global instructions that shape how Claude works with you. The example in this repo is personal—edit it to reflect your own working relationship.

---

## Adapting This

If you fork or copy this system:

1. **Edit `CLAUDE.md`** — The included version is specific to one person's working style. Write your own.
2. **Adjust the diary tone** — The spec calls for "journaling, not logging" but your preferred voice is yours.
3. **Consider what to track** — The schema has `decisions`, `open_items`, `notes_to_future_claude`. Add or remove fields based on what you actually want to remember.

The hooks are straightforward Python. Read `memory.py`—it's ~350 lines and does what you'd expect.

---

## Requirements

- Claude Code CLI
- Python 3.8+
- A willingness to let your AI assistant keep a diary
