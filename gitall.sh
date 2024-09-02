#!/bin/bash

bdir=$(realpath $(pwd))

BOLDGRAY="\e[1;37m"
ENDCOLOR="\e[0m"

for dir in ./*; do
    if [[ -d $dir ]]; then
        if [ "$dir" != "$(pwd)" ]; then
            cd "$dir"
            echo -e "${BOLDGRAY} ---------- $(pwd) ---------- ${ENDCOLOR}"
            git "$1"
            cd $bdir
	fi
    fi
done
