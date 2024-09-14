import numpy as np

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



print(data_stream_simulation())