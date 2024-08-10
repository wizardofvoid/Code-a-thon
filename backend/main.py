from data_preprocessing import load_and_preprocess_data
from train import train_model
from detect_anomalies import detect_anomalies
import tensorflow as tf

# Step 1: Load and preprocess data
file_path = "/Users/ivanpadeliya/Desktop/Data Set.xlsx"
data_scaled, scaler, label_encoders = load_and_preprocess_data(file_path)

# Step 2: Train the model
model, test_data = train_model(data_scaled)

# Step 3: Detect anomalies in the test data
anomalous_data_points, mse = detect_anomalies(model, test_data)

# Output results
print(f"Anomalous data points:\n{anomalous_data_points}")
