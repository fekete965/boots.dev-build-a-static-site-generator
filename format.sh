#!/bin/bash
# Format Python code using Black
# Usage: ./format.sh [--check]
#   --check: Check formatting without making changes

if [ "$1" == "--check" ]; then
    uv run black --check src/
else
    uv run black src/
fi

