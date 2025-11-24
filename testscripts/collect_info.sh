#!/bin/bash

# Prompt user for their details
echo "What is your name?"
read name

echo "How old are you?"
read age

echo "What is your ID number?"
read id

# Capture the current date and time (registration time)
time=$(date "+%Y-%m-%d %H:%M:%S")

# Capture the hostname using the 'hostname' command
hostname=$(hostname)

# Get the current terminal session info (username)
whoami=$(whoami)

# Save the output to a file
output_file="user_badge.txt"

# Write the output to the file, overwriting it with the first entry
echo "======== USER BADGE =========" > "$output_file"
echo "Thank you! Here is the information you provided:" >> "$output_file"
echo "Name: $name" >> "$output_file"
echo "Age: $age" >> "$output_file"
echo "ID number: $id" >> "$output_file"
echo "Registered: $time" >> "$output_file"
echo "Hostname: $hostname" >> "$output_file"
echo "Terminal: $whoami" >> "$output_file"
echo "============================" >> "$output_file"

# Optionally, show a message to the user that their info has been saved
echo "Your user badge information has been saved to $output_file."

