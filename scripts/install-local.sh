#!/bin/sh

set -eu

SCRIPT_DIR=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
REPO_DIR=$(CDPATH= cd -- "$SCRIPT_DIR/.." && pwd)
SOURCE_DIR="$REPO_DIR/skills"
CODEX_DEST_DIR=${CODEX_SKILLS_DIR:-"$HOME/.agents/skills"}
CLAUDE_DEST_DIR=${CLAUDE_SKILLS_DIR:-"$HOME/.claude/skills"}

work_dir=$(mktemp -d "${TMPDIR:-/tmp}/explorer-agent-skills-install.XXXXXX")
trap 'rm -rf "$work_dir"' EXIT HUP INT TERM
current="$work_dir/current"
: > "$current"

for skill_dir in "$SOURCE_DIR"/*; do
    [ -d "$skill_dir" ] || continue
    [ -f "$skill_dir/SKILL.md" ] || continue

    skill_name=$(basename -- "$skill_dir")
    printf '%s\t%s\n' "$skill_name" "$skill_dir" >> "$current"
done

install_to() {
    agent_name=$1
    dest_dir=$2
    manifest="$dest_dir/.explorer-agent-skills-links"

    mkdir -p "$dest_dir"
    printf '%s\n' "$agent_name ($dest_dir)"

    while IFS="$(printf '\t')" read -r skill_name skill_dir; do
        [ -n "$skill_name" ] || continue
        link_path="$dest_dir/$skill_name"

        if [ -L "$link_path" ]; then
            existing_target=$(readlink "$link_path")
            if [ "$existing_target" = "$skill_dir" ]; then
                printf 'unchanged  %s\n' "$skill_name"
            else
                printf 'conflict   %s (symlink points to %s)\n' "$skill_name" "$existing_target" >&2
            fi
        elif [ -e "$link_path" ]; then
            printf 'conflict   %s (path already exists and was left untouched)\n' "$skill_name" >&2
        else
            ln -s "$skill_dir" "$link_path"
            printf 'installed  %s\n' "$skill_name"
        fi
    done < "$current"

    if [ -f "$manifest" ]; then
        while IFS="$(printf '\t')" read -r old_name old_target; do
            [ -n "$old_name" ] || continue
            if ! awk -F '\t' -v name="$old_name" '$1 == name { found = 1 } END { exit !found }' "$current"; then
                old_link="$dest_dir/$old_name"
                if [ -L "$old_link" ] && [ "$(readlink "$old_link")" = "$old_target" ]; then
                    rm "$old_link"
                    printf 'removed    %s\n' "$old_name"
                else
                    printf 'preserved  %s (no longer an installer-owned symlink)\n' "$old_name" >&2
                fi
            fi
        done < "$manifest"
    fi

    cp "$current" "$manifest"
}

if [ ! -s "$current" ]; then
    printf 'No skills found in %s\n' "$SOURCE_DIR"
fi

install_to "Codex" "$CODEX_DEST_DIR"

if [ "$CLAUDE_DEST_DIR" = "$CODEX_DEST_DIR" ]; then
    printf 'Claude uses the same destination; skipped duplicate installation.\n'
else
    install_to "Claude Code" "$CLAUDE_DEST_DIR"
fi
