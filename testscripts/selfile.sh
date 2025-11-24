#!/bin/bash
for f in $(ls)
do
	if [ -d $f ]
	then
	 echo "$f" is a directori
 	fi
done
