import numpy as np
import tensorflow as tf

def detect_anomalies(model, test_data):
    # Example code, you need to replace it with your actual implementation
    predictions = model.predict(test_data)
    mse = np.mean(np.power(test_data - predictions, 2), axis=1)
    threshold = np.percentile(mse, 95)
    anomalies = mse > threshold
    anomalous_data_points = test_data[anomalies]  # Get actual data points that are anomalies
    return anomalous_data_points, mse
