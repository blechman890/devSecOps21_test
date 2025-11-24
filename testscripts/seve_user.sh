#!/bin/bash

full_name="$1"
user_email="$2"
user_id="$3"
registration_time=$4

machine="$HOSTNAME"

echo "======== USER BADGE ============"
echo "Name: $full_name"
echo "Email: $user_email"
echo "User ID: $user_id"
echo "Registered: $registration_time"
echo "Terminal: $machine"
echo "================================"


output_file="user_${full_name}.txt"


printf "======== USER BADGE ========\nName: %s\nEmail: %s\nUser ID: %s\nRegistered: %s\nTerminal: %s\n============================================\n" \
 "$full_name" "$user_email" "$user_id" "$registration_time" "$machine" > "$output_file"

# Optionally, show a message to the user
echo "User badge information has been saved to $output_file."

