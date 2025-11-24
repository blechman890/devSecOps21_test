#!/bin/bash

# Generate 3 random numbers between 1 and 100
num1=$((RANDOM % 100 + 1))
num2=$((RANDOM % 100 + 1))
num3=$((RANDOM % 100 + 1))

# Get the current username
user=$(whoami)

# Prepare the output message
message="The three lucky numbers for $user are: $num1, $num2, $num3"

# Echo the message
echo $message

# Append the output to lottery.log
echo $message >> lottery.log

