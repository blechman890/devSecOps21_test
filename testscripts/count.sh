#!/bin/bash

# Initialize counters and total size variable
file_count=0
dir_count=0
total_size=0

# Iterate over all items in the current directory
for item in *; do
    if [[ -f "$item" ]]; then
        # It's a regular file
        ((file_count++))
        # Get the size of the file in KB and add it to the total size
        file_size=$(stat -c %s "$item")
        ((total_size+=file_size))
    elif [[ -d "$item" ]]; then
        # It's a directory
        ((dir_count++))
    fi
done

# Calculate total size in KB (divide by 1024 to convert bytes to KB)
total_size_kb=$((total_size / 1024))

# Display a summary with colored output
echo -e "\nSummary of the current directory:"
echo -e "\e[32mTotal files: $file_count\e[0m"  # Green for files
echo -e "\e[33mTotal directories: $dir_count\e[0m"  # Yellow for directories
echo -e "\e[32mTotal size of files: $total_size_kb KB\e[0m"  # Green for total size

# Create backup directories using brace expansion
echo -e "\nCreating backup directories using brace expansion..."
mkdir -p backup_{1..5}
echo "Backup directories 'backup_1' to 'backup_5' created."

