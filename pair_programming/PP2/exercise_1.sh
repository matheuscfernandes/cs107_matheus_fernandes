#!/bin/bash
read -r -p "File name: " fn

git add $fn
git status

read -r -p "Do you wish to continue: (Y or N) " answer

if [ "$answer" = "N" ] || [ "$answer" = "n" ]; then
	exit
fi

read -r -p "Commit Message: " msg

git commit -m $msg

git status

read -r -p "Do you wish to continue: (Y or N) " answer

if [ "$answer" = "N" ] || [ "$answer" = "n" ]; then
	exit
fi

git push

