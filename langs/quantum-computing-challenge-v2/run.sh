#!/bin/sh

set -e

cat "$1" | sed -n 1p | base64 -d > judge.py
cat "$1" | sed -n 2p | base64 -d > solve.py

python3 sanitizer.py && python3 judge.py