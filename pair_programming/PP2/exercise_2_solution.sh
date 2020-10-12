#!/bin/bash
read -r -p "File to add:  " fadd
git add $fadd
git status
read -r -p "Do you wish to continue?  " cont
if [ "$cont" = "N" ]; then
    echo "Exiting"
    exit 1
fi
echo "OK."
read -r -p "Commit message:  " mess
git commit -m "$mess"
git status
read -r -p "Do you wish to continue?  " cont
if [ "$cont" = "N" ]; then
    echo "Exiting"
    exit 1
fi
git push
