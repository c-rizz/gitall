#!/usr/bin/env python3

import os
import sys
import subprocess

current_path = os.getcwd()

BOLDGRAY="\\e[1;37m"
ENDCOLOR="\\e[0m"


subfolders = [f for f in sorted(os.listdir(current_path)) if os.path.isdir(os.path.join(current_path, f))]
excludes_file = os.path.join(current_path, ".gitall_exclude")
includes_file = os.path.join(current_path, ".gitall_include")
has_excludes = os.path.exists(excludes_file)
has_includes = os.path.exists(includes_file)

if has_includes:
    with open(includes_file, 'r') as f:
        includes = [line.strip() for line in f if line.strip()]
    excludes = []
elif has_excludes:
    with open(excludes_file, 'r') as f:
        excludes = [line.strip() for line in f if line.strip()]
    includes = []
else:
    excludes = []
    includes = []

if len(includes) > 0:
    subfolders = includes
elif len(excludes) > 0:
    subfolders = [f for f in subfolders if f not in excludes]

for f in subfolders:
    f = os.path.join(current_path,f)
    print(f"\033[1m ---------- {f} ---------- \033[0m")
    # print(f"Running {['git']+sys.argv[1:]} in {f}")
    subprocess.run(['git']+sys.argv[1:], cwd=f)