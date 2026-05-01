#!/bin/sh

cp -f "$1" /tmp/code.cpp
g++ -std=c++23 /tmp/code.cpp -o "$2"