#!/bin/bash

bdir=$(realpath $(pwd))

BOLDGRAY="\e[1;37m"
ENDCOLOR="\e[0m"

for dir in ./*; do
    cd "$dir"
    echo -e "${BOLDGRAY} ---------- $(pwd) ---------- ${ENDCOLOR}"
    git "$1"
    cd $bdir
done
