import numpy as np
import tensorflow as tf

def detect_anomalies(model, test_data, scaler, threshold=95):
    # Predict using the model
    predictions = model.predict(test_data)

    # Calculate Mean Squared Error (MSE)
    mse = np.mean(np.power(test_data - predictions, 2), axis=1)

    # Determine the anomaly threshold
    threshold_value = np.percentile(mse, threshold)
    anomalies = mse > threshold_value

    return anomalies, mse
