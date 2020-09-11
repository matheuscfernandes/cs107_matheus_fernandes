#!/bin/bash
find . -maxdepth 1 -type f | awk -F/ '{print $NF}' | while read fname; do
	count_words=`wc -l < $fname`
	echo $fname $count_words
done
