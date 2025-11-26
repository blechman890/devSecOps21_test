#!/bin/bash

## Check if log file provided by the system

SYSLOG="/var/log/syslog"

# Check if file exists

if

 [[ ! -f "$SYSLOG" ]]; then
	echo "Syslog file not found at: $SYSLOG"
	exit 1
fi

timestamp=$(date +"%Y%m%d_%H%M%S")
epoch=$(date +%s)

report="syslog_report_${timestamp}.txt"
the_initiator=$whoami

## Report format

echo "===== LOG ANALYSIS REPORT =====" > "$report"
echo "Source log: $SYSLOG" >> "$report"
echo "Generated at: "$timestamp" >> "$report"
echo "Epoch date: "$epoch" >> "$report"
echo "Initiated by: "$the_initiator" >> "$report"

# What to search and send to the report
errcnt=$(grep -Ei "ERROR|FAILED|error|WARN|CRITICAL|critical" "$SYSLOG" | wc -l)
echo "Total number of errors: "$errcnt" >> "$report"

ip_extr= grep -Eo "([0-9]{1,3}\.){3}[0-9]{1,3}" "$SYSLOG" \
	| sort \
	| uniq -c \
	| sort -nr >> "$report"

