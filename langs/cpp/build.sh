#!/bin/sh

cp -f "$1" /tmp/code.cpp
g++ /tmp/code.cpp -o "$2"