#!/bin/bash

if [ -d d1 ] && cd d1
then
	printf "$PWD\n"
fi
