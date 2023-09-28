#!/usr/bin/env bash

# If any command fails, exit immediately with that command's exit status
set -e

# Find all changed files for this commit
# Compute the diff only once to save a small amount of time.
CHANGED_FILES=$(git diff --name-only --cached --diff-filter=ACMR)
# Get only changed files that match our file suffix pattern
get_pattern_files() {
    pattern=$(echo "$*" | sed "s/ /\$\\\|/g")
    echo "$CHANGED_FILES" | { grep "$pattern$" || true; }
}
# Get all changed python files
M_FILES=$(get_pattern_files .m)

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

echo SCRIPT_DIR=$SCRIPT_DIR
echo PWD=$PWD

if [[ -n "$M_FILES" ]]
then
    echo $M_FILES
fi