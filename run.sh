#!/bin/bash
set -e

python3 levels.py
mlg1 iwbtg/src/main.mlg1 build/compiled.g1  --include_source
g1a build/compiled.g1 build/assembled.g1b --data_path build/compiled.g1d
cg1  build/assembled.g1b --show_fps