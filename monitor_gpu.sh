#!/bin/bash

# Create a logs directory if it doesn't exist
mkdir -p logs

# Generate a unique filename based on the current timestamp
filename="gpu_power_log_$(date '+%Y%m%d_%H%M%S').csv"
filepath="./logs/$filename"
echo "timestamp,power usage,memory_usage" > $filepath


python plot_gpu_data.py $filepath &
PY_PID=$!

trap "kill $PY_PID; exit" SIGINT SIGTERM

while true; do
    timestamp=$(date '+%Y-%m-%d %H:%M:%S')
    power_usage=$(nvidia-smi -q -d POWER | grep -E "Power Draw" | grep -v "N/A" | awk '{print $4}')
    memory_usage=$(nvidia-smi --query-gpu=memory.used --format=csv,noheader,nounits)
    log_entry="$timestamp,$power_usage,$memory_usage"
    echo $log_entry >> $filepath
    sleep 2
done