#!/bin/bash

# Path to syslog file
SYSLOG_PATTERN="/var/log/syslog*"

# Check if file exists
if [[ ! -f "$SYSLOG_PATTERN" ]]; then
    echo "Syslog file not found at: $SYSLOG_PATTERN"
    exit 1
fi

if [[ ! -r "$SYSLOG_PATTERN" ]]; then
    echo "Don't have read permissions: $SYSLOG_PATTERN"
    exit 1
fi

timestamp=$(date +"%Y%m%d_%H%M%S")
epoch=$(date +%s)
report="syslog_report_${timestamp}.txt"
the_initiator=$(whoami)

# Report header
{
echo "===== LOG ANALYSIS REPORT ====="
echo "Source log: $SYSLOG_PATTERN"
echo "Generated at: $timestamp"
echo "Epoch date: $epoch"
echo "Initiated by: $the_initiator"
echo ""
} > "$report"

# Loop over all syslog files
for log in $SYSLOG_PATTERN; do
    if [[ -f "$log" && -r "$log" ]]; then
        echo "Processing $log"


# Count errors/warnings
errcnt=$(grep -Ei "error|failed|warn|critical" "$log" | wc -l)
echo "Total number of errors: $errcnt" >> "$report"
echo "" >> "$report"

# Extract IP addresses and their counts
echo "===== IP ADDRESS FREQUENCY =====" >> "$report"
grep -Eo "([0-9]{1,3}\.){3}[0-9]{1,3}" "$log" \
    | sort \
    | uniq -c \
    | sort -nr >> "$report"

echo "Report saved to: $report"

