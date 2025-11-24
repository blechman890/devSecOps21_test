#!/bin/bash

while true; do


	read -rp "Enter a number between 0 and 100: " number
		## -r = do not allow backlash and escapes
		## -p = prompt a user for input
		## number = A variable that stores user's input
## Validating that the input is indeed a number

	if ! [[ "$number" =~ ^[0-9]+$ ]]; then
	## [[ ... ]] is Bash’s advanced test command. =~ means "matches regex" = regular expression.
	## ^ = start of string, $ = end of string. [0-9] means digits between 0 and 9.
	## In general, that means that the input must be a sequence of digits ONLY.
	## ! negates the condition, so the block runs when the input is NOT a number.
	
	echo "Invalid input..."
	continue
		## Continue = will run to the top of the loop (It repeats from the start if)

	fi

## Check if the entered number is within the allowed range
	if (( number >= 0 && number <= 100 )); then
		break
	else 
	    echo "Number not in range 0-100. Try again."
	fi

## (( ... )) is arithmetic evaluation in Bash.
## Inside it:
## Variables do not need $
## Logical operators work like in C (&&, >=, <=)

done

## Range check

if 
	(( number >= 0 && number <= 29 )); then
	echo "The number $number is between 0 and 29."
elif	(( number >= 30 && number <= 59 )); then
	echo "The number $number is between 30 and 59."
elif	(( number >= 60 && number <= 89 )); then
	echo "the number $number is between 60 and 89."
elif 	(( number >= 90 && number <= 100 )); then
	echo "The number $number is between 90 and 100."

fi
