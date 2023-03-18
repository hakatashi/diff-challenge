#!/bin/sh

cat "$1" | sed -n 1p | base64 -d > a
cat "$1" | sed -n 2p | base64 -d > b

./build.sh a a.out
./build.sh b b.out

./compare a.out b.out