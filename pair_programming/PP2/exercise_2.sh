#!/bin/bash

#Sharer: Matt Fernandes
#Coder: Matt Fernandes
#Listener: Chenfan Zhuang

for file in $( ls )
do
	perm=$( ls -l $file )  
	exec=${perm:3:1}
	if [ "$exec" = "x" ]; then
		echo 'user has permission to execute' $file
	else
		echo 'user does not have permission to execute' $file
	fi
done

