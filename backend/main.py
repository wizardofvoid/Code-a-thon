from data_preprocessing import load_and_preprocess_data
from train import train_model
from detect_anomalies import detect_anomalies
import tensorflow as tf

# Step 1: Load and preprocess data
data_scaled, scaler = load_and_preprocess_data('Data.csv')

# Step 2: Train the model
model, test_data = train_model(data_scaled)

# Step 3: Detect anomalies in the test data
anomalies, mse = detect_anomalies(model, test_data, scaler)

# Output results
print(f"Number of anomalies detected: {sum(anomalies)}")
