#!/bin/sh

# Usage: script <submitted ELF binary> < testcase input
# Executes the submitted binary as-is with a per-testcase time limit of 2 seconds.

# Only ELF files are accepted (otherwise shell scripts could be executed via shebang or the ENOEXEC fallback)
if [ "$(head -c 4 "$1" | od -An -tx1 | tr -d ' \n')" != "7f454c46" ]; then
  echo "Not an ELF file" >&2
  exit 126
fi

chmod +x "$1"
exec timeout -s KILL 2 "$1"
