import matplotlib
matplotlib.use('TkAgg')
import matplotlib.animation as animation
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd
import signal
import sys
import os

MAX_GPU = 8192
MAX_WATT = 220

def get_latest_csv(directory):
    # List all CSV files in the directory
    csv_files = [f for f in os.listdir(directory) if f.endswith('.csv')]
    
    # Return the latest (most recent) CSV file
    return os.path.join(directory, sorted(csv_files, reverse=True)[0])

def signal_handler(sig, frame):
    plt.close('all')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

def animate(i):
    data = pd.read_csv(get_latest_csv('./logs')).tail(60)
    
    # Clear the data on each axis
    ax1.clear()
    ax2.clear()
    
    data['timestamp'] = pd.to_datetime(data['timestamp'])  
    time_format = mdates.DateFormatter('%H:%M:%S')  
    
    ax1.plot(data['timestamp'], data['power usage'], label='Power Usage (W)')
    ax1.axhline(y=MAX_WATT, color='r', linewidth=2, label=f'Max Power ({MAX_WATT})')
    ax1.legend(loc='upper right')
    ax1.set_ylim([0, MAX_WATT]) 
    ax1.set_yticks(range(0, MAX_WATT-1, 20))  

    ax2.plot(data['timestamp'], data['memory_usage'], label='Memory Usage (MiB)')
    ax2.axhline(y=MAX_GPU, color='r', linewidth=2, label=f'Max Memory ({MAX_GPU}MiB)')
    ax2.legend(loc='upper right')
    
    ax2.xaxis.set_major_formatter(time_format)  
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

ani = animation.FuncAnimation(fig, animate, interval=2000, save_count=100)

plt.tight_layout()
plt.show()
