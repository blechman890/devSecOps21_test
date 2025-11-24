#!/bin/bash

# Check if a file name is provided as an argument
if [ -z "$1" ]; then
    echo "Usage: $0 <filename>"
    exit 1
fi

# Get the file name from the first argument
filename="$1"

# Check if the file exists
if [ ! -f "$filename" ]; then
    echo "File '$filename' does not exist."
    exit 1
fi

# Count the number of lines in the file
line_count=$(wc -l < "$filename")

# Count the number of words in the file
word_count=$(wc -w < "$filename")

# Get the file size in bytes
file_size=$(stat --format="%s" "$filename")

# Get the file usage size using du command (in KB)
file_usage_size=$(du -k "$filename" | cut -f1)

# Safely display the information using printf
printf "File Information for '%s':\n" "$filename"
echo --------------------------------
printf "Number of Lines   : %d\n" "$line_count"
printf "Number of Words   : %d\n" "$word_count"
printf "File Size (bytes) : %d\n" "$file_size"
printf "File Usage Size   : %d KB\n" "$file_usage_size"
printf "\n"

# Save the output to fileinfo.log
{
    printf "File Information for '%s':\n" "$filename"
echo "----------------------------------"
    printf "Number of Lines   : %d\n" "$line_count"
    printf "Number of Words   : %d\n" "$word_count"
    printf "File Size (bytes) : %d\n" "$file_size"
    printf "File Usage Size   : %d KB\n" "$file_usage_size"
    printf "\n"
} >> fileinfo.log

