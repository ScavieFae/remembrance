#!/bin/bash
#
# Claude Code Configuration Installer
#
# This script installs your custom Claude Code setup by symlinking
# configuration files to ~/.claude/
#
# Usage: ./install.sh
#

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CLAUDE_DIR="$HOME/.claude"

echo "Installing Claude Code configuration..."
echo "Source: $SCRIPT_DIR"
echo "Target: $CLAUDE_DIR"
echo ""

# Create ~/.claude if it doesn't exist
mkdir -p "$CLAUDE_DIR"
mkdir -p "$CLAUDE_DIR/memories/sessions"

# Backup existing files if they exist and aren't symlinks
backup_if_exists() {
    local file="$1"
    if [ -e "$file" ] && [ ! -L "$file" ]; then
        local backup="${file}.backup.$(date +%Y%m%d_%H%M%S)"
        echo "  Backing up existing $file to $backup"
        mv "$file" "$backup"
    elif [ -L "$file" ]; then
        echo "  Removing existing symlink $file"
        rm "$file"
    fi
}

# Install settings.json
echo "Installing settings.json..."
backup_if_exists "$CLAUDE_DIR/settings.json"
ln -s "$SCRIPT_DIR/settings.json" "$CLAUDE_DIR/settings.json"
echo "  ✓ Linked settings.json"

# Install hooks directory
echo "Installing hooks..."
backup_if_exists "$CLAUDE_DIR/hooks"
ln -s "$SCRIPT_DIR/hooks" "$CLAUDE_DIR/hooks"
echo "  ✓ Linked hooks/"

echo ""
echo "Installation complete!"
echo ""
echo "What was installed:"
echo "  • settings.json - Model preferences and hook configuration"
echo "  • hooks/memory.py - Persistent memory system"
echo ""
echo "What stays local to this machine:"
echo "  • ~/.claude/memories/ - Your session memories (not synced)"
echo ""
echo "To verify, run: ls -la ~/.claude/"
