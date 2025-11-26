#!/bin/bash
set -x
# Path to syslog file pattern
SYSLOG_PATTERN="/var/log/syslog*"
CONFIG_FILE="error_keywords.conf"

# Check if the configuration file exists
if [[ ! -f "$CONFIG_FILE" ]]; then
    echo "Error: Configuration file '$CONFIG_FILE' not found."
    exit 1
fi

# Load error patterns from config file
ERROR_PATTERNS=$(cat "$CONFIG_FILE")

# Check if files matching the pattern exist
if ! ls $SYSLOG_PATTERN &>/dev/null; then
    echo "Syslog files not found matching pattern: $SYSLOG_PATTERN"
    exit 1
fi

# Check if the syslog files are readable
for log in $SYSLOG_PATTERN; do
    if [[ ! -r "$log" ]]; then
        echo "Don't have read permissions on $log"
        exit 1
    fi
done

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

# Loop over all syslog files matching the pattern
for log in $SYSLOG_PATTERN; do
    if [[ -f "$log" && -r "$log" ]]; then
        echo "Processing $log"

	# Add a section header for each log file
	echo "===== Analysis for Log: $log =====" >> "$report"
	echo "" >> "$report" # Blank line for clarity
	
        # Count anomalies dynamically based on loaded patterns
for pattern in $ERROR_PATTERNS; do
        errcnt=$(grep -Ei "$pattern" "$log" | wc -l)
        echo "Total number of occurences for '$pattern' : $errcnt" >> "$report"
        echo "" >> "$report"
done
        # Extract IP addresses and their counts
        echo "===== IP ADDRESS FREQUENCY =====" >> "$report"
        grep -Eo "([0-9]{1,3}\.){3}[0-9]{1,3}" "$log" \
            | sort \
            | uniq -c \
            | sort -nr >> "$report"

    else
        echo "Skipping $log: File does not exist or is not readable."
    fi
done

echo "Report saved to: $report"

