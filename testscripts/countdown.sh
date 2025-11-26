#!/bin/bash

while true; do

# Ask the user for a directory name
read -rp "Enter a directory name: " dirname

# Check if directory exists
if [ -d "$dirname" ]; then
    echo "Directory '$dirname' exists. Proceeding…"

    sleep 5
    cd "$dirname" || { echo "Failed to enter directory."; exit 1; }

    sleep 3
    printf "The end\n"
else
    echo "Directory '$dirname' does not exist."
fi
done
