#!/bin/sh

set -e

cat "$1" | sed -n 1p | base64 -d > problem.py
cat "$1" | sed -n 2p | base64 -d > circuit.py

python3 sanitizer.py && python3 problem.py