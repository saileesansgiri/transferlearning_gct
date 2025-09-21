# Transfer Learning GCT – Visualization Sample

This repository provides a visualization script and sample dataset for ground contact time (GCT) detection and IMU signals during walking.  
It demonstrates how to plot concurrent vertical accelerometer data with ground truth ground contact from different walking conditions, with 10 steps per leg sampled at 100 Hz.

---

## Files
- `visualization_sample.py` – Python script for plotting Right GCT and vertical acceleration signals.
- `sample_gct_walk.xlsx` – Example dataset containing short gait segments from multiple walking conditions.

---

## Data Description

The Excel file `sample_gct_walk.xlsx` contains five sheets, each representing a different walking condition:

1. `sample_treadmill_walk_young` – Treadmill walking, younger adults  
2. `sample_treadmill_walk` – Treadmill walking, older adults  
3. `sample_overground_level_walk` – Overground level walking, older adults  
4. `sample_overground_incline` – Overground incline walking, older adults  
5. `sample_overground_decline` – Overground decline walking, older adults  

### Columns in each sheet:
- `Right_GCT` – Binary sequence marking right-leg ground contact  
- `Left_GCT` – Binary sequence marking left-leg ground contact  
- `Acc_r_x`, `Acc_r_y`, `Acc_r_z` – Raw accelerometer signals from the right foot IMU (x, y, z axes)  
- `Acc_l_x`, `Acc_l_y`, `Acc_l_z` – Raw accelerometer signals from the left foot IMU (x, y, z axes)  
- `Gyr_r_x`, `Gyr_r_y`, `Gyr_r_z` – Raw gyroscope signals from the right foot IMU (x, y, z axes)  
- `Gyr_l_x`, `Gyr_l_y`, `Gyr_l_z` – Raw gyroscope signals from the left foot IMU (x, y, z axes)  

For visualization, the script uses only the **z-axis accelerometer data** (`Acc_r_z` and optionally `Acc_l_z`).  
Data were sampled at 100 Hz using foot-mounted IMUs.

---

## Visualization

The script:
- Applies a 4th-order Butterworth low-pass filter (cutoff = 6 Hz) to the acceleration signals for smoother visualization.  
- Plots Right GCT (solid blue line) alongside filtered right-foot vertical acceleration (orange line).  
- Optionally, Left GCT and left-foot vertical acceleration can also be visualized (commented lines in code).  
- Produces one plot per walking condition with consistent formatting.

Example plot:
- X-axis: Frames (time samples at 100 Hz)  
- Left Y-axis: Ground contact (binary)  
- Right Y-axis: Vertical acceleration (m/s²)  

---

## Requirements

The script requires the following Python packages:
- pandas
- numpy
- matplotlib
- scipy

Install them with:

```bash
pip install pandas numpy matplotlib scipy
