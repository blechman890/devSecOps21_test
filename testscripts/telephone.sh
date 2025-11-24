#!/bin/bash

# Path to the dictionary file (standard location in Unix-like systems)
DICTIONARY="/usr/share/dict/words"

# Check if the dictionary file exists
if [[ ! -f "$DICTIONARY" ]]; then
    echo "Dictionary file not found!"
    exit 1
fi

# Ask the user to input a word
echo "Enter a word to check:"
read user_word

# Get the line number of the word 'telephone' in the dictionary
telephone_line=$(grep -n "^telephone$" "$DICTIONARY" | cut -d: -f1)

# If 'telephone' is not found in the dictionary
if [[ -z "$telephone_line" ]]; then
    echo "'telephone' is not found in the dictionary!"
    exit 1
fi

# Check if the word appears after 'telephone' in the dictionary
word_found=$(tail -n +"$telephone_line" "$DICTIONARY" | grep -x "$user_word")

# Output result
if [[ -n "$word_found" ]]; then
    echo "✔ The word '$user_word' appears after 'telephone' in the dictionary."
else
    echo "✘ The word '$user_word' does not appear after 'telephone' in the dictionary."
fi

