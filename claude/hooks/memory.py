#!/usr/bin/env python3
"""
Claude Code Memory System
Handles persistent memory across sessions via hooks.

Usage:
  python3 memory.py load    # SessionStart: Load recent memories
  python3 memory.py save    # SessionEnd: Save session summary
"""

import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

# Configuration
MEMORIES_DIR = Path.home() / ".claude" / "memories" / "sessions"
MAX_SESSIONS = 50  # Keep last N sessions
SESSIONS_TO_LOAD = 10  # Show N most recent on startup


def get_memories_dir():
    """Ensure memories directory exists and return path."""
    MEMORIES_DIR.mkdir(parents=True, exist_ok=True)
    return MEMORIES_DIR


def load_memories():
    """Load and display recent session memories for SessionStart hook."""
    memories_dir = get_memories_dir()

    # Get all session files, sorted by timestamp (newest first)
    session_files = sorted(
        memories_dir.glob("*.json"),
        key=lambda f: f.stat().st_mtime,
        reverse=True
    )[:SESSIONS_TO_LOAD]

    if not session_files:
        # No memories yet
        sys.exit(0)

    # Format memories for Claude
    print("=== Memory from Previous Sessions ===\n")

    for session_file in session_files:
        try:
            with open(session_file) as f:
                memory = json.load(f)

            timestamp = memory.get("timestamp", "Unknown date")
            if "T" in timestamp:
                # Parse ISO format and make readable
                dt = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
                timestamp = dt.strftime("%b %d, %Y %H:%M")

            project = memory.get("project", "Unknown project")
            # Shorten home directory for readability
            project = project.replace(str(Path.home()), "~")

            summary = memory.get("summary", "No summary available")
            tasks = memory.get("tasks_completed", [])
            files = memory.get("files_modified", [])

            print(f"[{timestamp} - {project}]")
            print(f"{summary}")

            if tasks:
                print(f"Tasks: {', '.join(tasks[:3])}")

            if files:
                # Show abbreviated file paths
                short_files = [f.split("/")[-1] for f in files[:5]]
                print(f"Files: {', '.join(short_files)}")

            print()

        except (json.JSONDecodeError, KeyError) as e:
            # Skip corrupted files
            continue

    sys.exit(0)


def extract_files_from_transcript(messages):
    """Extract file paths mentioned in the transcript."""
    files = set()

    # Patterns for file paths
    file_patterns = [
        r'(?:Read|Write|Edit|Glob)\s+(?:file[:\s]+)?["\']?([/~][^\s"\']+)',
        r'(?:created|modified|edited|updated|reading|wrote)\s+["\']?([/~][^\s"\']+)',
        r'`([/~][^`\s]+\.[a-z]+)`',
    ]

    text = json.dumps(messages)

    for pattern in file_patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        files.update(matches)

    # Filter to likely real files (have extensions or are common paths)
    valid_files = [
        f for f in files
        if "." in f.split("/")[-1] or f.endswith("/")
    ]

    return list(valid_files)[:10]


def extract_user_messages(messages):
    """Extract user messages from transcript."""
    user_msgs = []

    for msg in messages:
        if msg.get("role") == "user":
            content = msg.get("content", "")
            if isinstance(content, list):
                # Handle structured content
                text_parts = [
                    p.get("text", "") for p in content
                    if isinstance(p, dict) and p.get("type") == "text"
                ]
                content = " ".join(text_parts)

            if content and len(content) > 10:
                # Truncate long messages
                user_msgs.append(content[:200])

    return user_msgs


def extract_topics(user_messages, files):
    """Extract likely topics/keywords from the session."""
    topics = set()

    # Common tech keywords to look for
    keywords = [
        "api", "database", "auth", "test", "bug", "fix", "feature",
        "refactor", "deploy", "config", "docker", "git", "react",
        "python", "javascript", "typescript", "rust", "go", "java",
        "frontend", "backend", "server", "client", "hook", "memory",
        "build", "install", "setup", "debug", "error", "performance"
    ]

    text = " ".join(user_messages).lower()

    for keyword in keywords:
        if keyword in text:
            topics.add(keyword)

    # Add file extensions as topics
    for f in files:
        if "." in f:
            ext = f.split(".")[-1].lower()
            if ext in ["py", "js", "ts", "tsx", "jsx", "rs", "go", "java", "rb"]:
                topics.add(ext)

    return list(topics)[:10]


def generate_summary(user_messages):
    """Generate a brief summary from user messages."""
    if not user_messages:
        return "Session with no recorded user messages"

    # Use first few user messages to create summary
    combined = " | ".join(user_messages[:3])

    # Truncate to reasonable length
    if len(combined) > 300:
        combined = combined[:297] + "..."

    return combined


def save_memory():
    """Save session summary for SessionEnd hook."""
    memories_dir = get_memories_dir()

    # Read hook input from stdin
    try:
        hook_input = json.load(sys.stdin)
    except json.JSONDecodeError:
        # No valid input, create minimal record
        hook_input = {}

    session_id = hook_input.get("session_id", "unknown")
    transcript_path = hook_input.get("transcript_path", "")
    cwd = hook_input.get("cwd", os.getcwd())

    # Try to read transcript
    messages = []
    if transcript_path and Path(transcript_path).exists():
        try:
            with open(transcript_path) as f:
                transcript = json.load(f)
                messages = transcript if isinstance(transcript, list) else []
        except (json.JSONDecodeError, IOError):
            pass

    # Extract information
    user_messages = extract_user_messages(messages)
    files_modified = extract_files_from_transcript(messages)
    topics = extract_topics(user_messages, files_modified)
    summary = generate_summary(user_messages)

    # Create memory record
    timestamp = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    memory = {
        "session_id": session_id,
        "timestamp": timestamp,
        "project": cwd,
        "summary": summary,
        "tasks_completed": user_messages[:5],  # Use user requests as "tasks"
        "files_modified": files_modified,
        "topics": topics
    }

    # Save to timestamped file
    filename = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S") + ".json"
    memory_file = memories_dir / filename

    with open(memory_file, "w") as f:
        json.dump(memory, f, indent=2)

    # Cleanup old sessions
    cleanup_old_sessions(memories_dir)

    sys.exit(0)


def cleanup_old_sessions(memories_dir):
    """Remove sessions beyond MAX_SESSIONS limit."""
    session_files = sorted(
        memories_dir.glob("*.json"),
        key=lambda f: f.stat().st_mtime,
        reverse=True
    )

    # Delete files beyond the limit
    for old_file in session_files[MAX_SESSIONS:]:
        try:
            old_file.unlink()
        except IOError:
            pass


def main():
    if len(sys.argv) < 2:
        print("Usage: memory.py [load|save]", file=sys.stderr)
        sys.exit(1)

    command = sys.argv[1].lower()

    if command == "load":
        load_memories()
    elif command == "save":
        save_memory()
    else:
        print(f"Unknown command: {command}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
