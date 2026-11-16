#!/bin/sh

# Usage: script <submitted ELF binary> < testcase input
# Executes the submitted binary as-is with a per-testcase time limit of 2 seconds.

# Only 32-bit x86 (i386) ELF files are accepted:
# - bytes 0..3: 7f 45 4c 46 (\x7fELF magic; prevents shell script execution via shebang / ENOEXEC fallback)
# - byte 4 (e_ident[EI_CLASS]): 01 (ELFCLASS32)
# - byte 5 (e_ident[EI_DATA]): 01 (ELFDATA2LSB)
# - bytes 18..19 (e_machine): 03 00 (EM_386)
if [ "$(head -c 6 "$1" | od -An -tx1 | tr -d ' \n')" != "7f454c460101" ] || \
   [ "$(dd if="$1" bs=1 skip=18 count=2 2>/dev/null | od -An -tx1 | tr -d ' \n')" != "0300" ]; then
  echo "Not a 32-bit x86 ELF file" >&2
  exit 126
fi

chmod +x "$1"
exec timeout -s KILL 2 "$1"
