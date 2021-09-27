#!/bin/bash
set -e

python main.py data/test3.txt graphs/test.jgr
scp graphs/test.jgr hydra:~/Documents
read
scp hydra:~/Documents/test1.jpg graphs/
open graphs/test1.jpg
