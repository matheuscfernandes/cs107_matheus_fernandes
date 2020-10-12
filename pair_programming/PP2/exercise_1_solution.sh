#!/bin/bash
for f in $( ls ); do
        if [ -x $f ]; then
                echo $f "is executable"
        fi
done
