for n in a b c d e
do
	while true
	do
		if [ $RANDOM -gt 20000 ]
		then
			printf .
			break 2 ## break out of both while and for loops
		elif [ $RANDOM -lt 10000 ]
		then
			printf '"'
		fi
	done
done
