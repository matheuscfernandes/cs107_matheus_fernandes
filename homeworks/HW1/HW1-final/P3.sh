#!/bin/bash
grep -c "[0-9]" apollo13.txt > apollo_out.txt
grep --help | grep "^  -c"
ls *.py | wc -l
find . -type f ! -perm -o+w,o+r | wc -l
find . -maxdepth 1 ! -perm -o+w,o+r | wc -l
