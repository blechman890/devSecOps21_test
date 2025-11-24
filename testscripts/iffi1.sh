#!/bin/bash

read name
if [ -z "$name" ]
then
echo "No name entered" >&2
exit 1
elif [ $name != Ilya ]
then
	printf "You are the worse!\n"
elif [ $name = "Ilya" ]
then 
	printf "Ilya is the best\n"
else
	echo "You have entered $name"
fi 
