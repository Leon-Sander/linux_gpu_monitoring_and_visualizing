# GPU Monitoring Tool

A simple GPU monitoring tool that logs GPU power and memory usage in real-time and visualizes the data using a matplotlib plot.

## Overview

This tool consists of two main parts:
1. A bash script that continuously logs GPU power and memory usage to a CSV file.
2. A Python script that reads the latest CSV logs and visualizes the GPU power and memory usage using a real-time plot.

## Prerequisites

- NVIDIA GPU
- `nvidia-smi` utility
- Python 3.x
- Libraries: `matplotlib`, `pandas`

## Setup

1. Ensure you have `nvidia-smi` installed and available in your PATH.
2. Install the required Python libraries using pip:
3. Install python3-tk
```
pip install -r requirements.txt & sudo apt-get install python3-tk
```



## Usage

1. Make the bash script executable:

```
chmod +x monitor_gpu.sh
```

2. Run the bash script:

```
./monitor_gpu.sh
```


This will create a unique CSV log file under the `./logs/` directory for each run. The Python script will visualize the latest log data in real-time using a matplotlib plot.

## Features

- Logs GPU power and memory usage every 2 seconds.
- Visualization updates every 2 seconds with the latest 60 data points.
- Red lines in the plots indicate the maximum power and memory capacities.

## Note

The maximum GPU memory and power capacities are set as constants (`MAX_GPU` and `MAX_WATT`) in the Python script. Adjust these values based on your GPU specifications if necessary.

## Stopping the Tool

Use `Ctrl+C` to gracefully terminate both the logging and visualization processes.

