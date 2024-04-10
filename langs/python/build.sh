#!/bin/sh

cp -f "$1" /tmp/code.py
~/.pyenv/versions/3.12.2/bin/python -m py_compile /tmp/code.py
cp -f /tmp/__pycache__/code.cpython-312.pyc "$2"