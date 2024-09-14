import numpy as np
from scipy.stats import zscore

import matplotlib.pyplot as plt
from collections import deque
import time

# Function to simulate the real-time data stream
def data_stream_simulation(size=1000, seasonal=True):
   """
   Simulates a data stream with noise and occasional anomalies.
   
   Parameters:
      size (int): The number of data points to generate.
      seasonal (bool): Whether to include a sinusoidal pattern in the data.
   
   Returns:
      numpy.ndarray: Simulated data stream with potential anomalies.
   """
   t = np.linspace(0, 100, size)  # Generate time steps
   data = 10 * np.sin(t) if seasonal else 5 * np.ones(size)  # Sinusoidal or flat trend
   noise = np.random.normal(0, 2, size)  # Add random noise
   anomalies = np.random.choice([0, 20], size=size, p=[0.98, 0.02])  # 2% chance of anomalies
   return data + noise + anomalies  # Combine the normal data with anomalies


# Function to detect anomalies using Z-score
def z_score_anomaly_detection(window, threshold=3):
   """
   Detect anomalies in the data stream using Z-Score.
   
   Parameters:
      window (list or np.ndarray): The current window of data.
      threshold (float): The Z-Score threshold to consider a point an anomaly.
   
   Returns:
      np.ndarray: Boolean array indicating whether each point is an anomaly.
   """
   z_scores = zscore(window)  # Compute Z-scores for the window
   anomalies = np.abs(z_scores) > threshold  # Flag points with Z-score > threshold
   return anomalies
