#Plots of the Right GCT and vertical accelerometer signal for 1. treadmill walking (younger adults), 2. treadmill walking (older adults), 3. overground level walking (older adults),
# 4. overground incline walking (older adults) and 5. overground decline walking (older adults)
#Sailee Sansgiri 2025

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

# Arbitrary low-pass filter for better visualization
def butter_lowpass_filter(data, cutoff, fs, order=4):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    y = filtfilt(b, a, data)
    return y

# Load the Excel file with the data
excel_file_path = r".\sample_gct_walk.xlsx"
xls = pd.ExcelFile(excel_file_path)

# Read each sheet into a dictionary of DataFrames
dfs = {sheet_name: xls.parse(sheet_name) for sheet_name in xls.sheet_names}

# Correct the column names in case of any leading/trailing whitespaces
dfs = {sheet_name: df.rename(columns=lambda x: x.strip()) for sheet_name, df in dfs.items()}

#plot titles
titles = {
    'sample_treadmill_walk_young': 'Treadmill Walking - Younger Adults',
    'sample_treadmill_walk': 'Treadmill Walking - Older Adults',
    'sample_overground_level_walk': 'Overground Level Walking - Older Adults',
    'sample_overground_incline': 'Overground Incline Walking - Older Adults',
    'sample_overground_decline': 'Overground Decline Walking - Older Adults'
}

# Sampling frequency of IMUs=100 Hz
fs = 100.0  # Sampling frequency in Hz
cutoff = 6 # Cutoff frequency in Hz

# Custom colors in hex
gct_color = '#0072BD'  # blue
acc_color = '#EF9336'  # orange

# Apply the filter to the acceleration data and plot the results
for sheet_name, df in dfs.items():
    df['Acc_r_z_filtered'] = butter_lowpass_filter(df['Acc_r_z'], cutoff, fs)
    df['Acc_l_z_filtered'] = butter_lowpass_filter(df['Acc_l_z'], cutoff, fs)
    
    fig, ax1 = plt.subplots(figsize=(12, 6))
    
    # Plot Right GCT and Left GCT on the primary y-axis
    ax1.plot(df['Right_GCT'], label='Right GCT', color=gct_color)
    
    #Remove comment to plot Left GCT
    # ax1.plot(df['Left_GCT'], label='Left GCT', color=gct_color, linestyle='dashed')

    ax1.set_xlabel('Frames')
    ax1.set_ylabel('Ground contact', color=gct_color)
    ax1.tick_params(axis='y', labelcolor=gct_color)
    
    # Create a secondary y-axis for the accelerometer data
    ax2 = ax1.twinx()
    ax2.plot(df['Acc_r_z_filtered'], label='Acc(z)', color=acc_color)

    #Remove comment to plot Left Accelerometer signal
    # ax2.plot(df['Acc_l_z_filtered'], label='Acc(z)', color=acc_color, linestyle='dashed')

    ax2.set_ylabel('Vertical acceleration signal', color=acc_color)
    ax2.tick_params(axis='y', labelcolor=acc_color)
    ax1.set_xlim(left=0)  # Set x-axis limit to start from 0
    
    # Add legends for both y-axes
    lines, labels = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines + lines2, labels + labels2, loc='upper right')

    
    #set title
    title = titles.get(sheet_name, sheet_name)
    ax1.set_title(title)
    ax1.grid(True,linestyle='--')
    
    # Adjust layout
    plt.tight_layout()
    plt.show()
