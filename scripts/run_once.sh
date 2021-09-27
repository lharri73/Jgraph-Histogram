#!/bin/bash
set -e

python main.py $1 graphs/test.jgr
scp graphs/test.jgr hydra:~/Documents
read
scp hydra:~/Documents/test1.jpg graphs/
open graphs/test1.jpg
