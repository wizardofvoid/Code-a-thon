import os
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder

def load_and_preprocess_data(filepath):
    # Check if the file exists and is accessible
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    
    if not os.access(filepath, os.R_OK):
        raise PermissionError(f"No read access to file: {filepath}")
    
    # Load the data
    data = pd.read_excel(filepath)
    
    # Convert categorical features to numeric using Label Encoding
    label_encoders = {}
    for column in ['Machine', 'Component', 'Parameter']:
        le = LabelEncoder()
        data[column] = le.fit_transform(data[column])
        label_encoders[column] = le
    
    # Drop non-numeric or irrelevant columns (like Id and Time)
    data = data.drop(columns=['Id', 'Time'])
    
    # Handle any missing values by removing them
    data = data.dropna()
    
    # Check if 'Value' column exists and needs to be scaled
    if 'Value' in data.columns:
        columns_to_scale = [col for col in data.columns if col != 'Value']
    else:
        columns_to_scale = data.columns
    
    # Scale the data
    scaler = StandardScaler()
    data[columns_to_scale] = scaler.fit_transform(data[columns_to_scale])
    
    return data, scaler, label_encoders
