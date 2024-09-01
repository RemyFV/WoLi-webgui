#!/bin/bash

echo "Content-type: text/html"
echo ""

# Read parameters from query string
MAC=$(echo "$QUERY_STRING" | grep -oE 'mac=[^&]+' | cut -d'=' -f2)
IP=$(echo "$QUERY_STRING" | grep -oE 'ip=[^&]+' | cut -d'=' -f2)
PORT=$(echo "$QUERY_STRING" | grep -oE 'port=[^&]+' | cut -d'=' -f2)

# Set default port if not specified
if [ -z "$PORT" ]; then
    PORT="9"
fi

# Send the magic packet if MAC is provided
if [ -n "$MAC" ]; then
    # Send the magic packet using netcat (nc)
    COMMAND="echo -e \$(echo \$(printf 'f%.0s' {1..12}; printf \"$MAC%.0s\" {1..16}) | sed -e 's/../\\\\x&/g') | nc -w1 -u $IP $PORT"
    eval $COMMAND

    # Output result
    echo "<html><body><p>Magic packet sent to $MAC via $IP:$PORT</p></body></html>"
else
    echo "<html><body><p>Missing MAC address parameter!</p></body></html>"
fi
