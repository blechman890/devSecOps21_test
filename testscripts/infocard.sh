#!/bin/bash

full_name=$1
age=$2
city=$3


echo "Full Name: $full_name"
echo "Age: $age"
echo "City: $city"

printf "Nmae: %s\nAge %s\City %s\n" "$name" "$age" "$city" > profile.txt

echo "Number of parameters: $#"
