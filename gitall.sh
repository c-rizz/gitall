#!/bin/bash

bdir=$(realpath $(pwd))

for dir in ./*; do
    cd "$dir"
    echo " ---------- $(pwd) ----------"
    git "$1"
    cd $bdir
done
