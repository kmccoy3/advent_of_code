#!/bin/bash

cd /Users/kmm12/Documents/documents-main/personal/coding/advent_of_code;

hyperfine 'python3 ./2023/day_1/day_1.py' \
'python3 ./2023/day_2/day_2.py' \
'python3 ./2023/day_3/day_3.py' \
'python3 ./2023/day_4/day_4.py' \
--export-markdown times.md --warmup 3;
