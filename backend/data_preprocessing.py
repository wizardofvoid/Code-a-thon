import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder

def load_and_preprocess_data(filepath):
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
    
    # Scale the data
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data)
    
    # Convert scaled data back to DataFrame
    data_scaled = pd.DataFrame(data_scaled, columns=data.columns)
    
    return data_scaled, scaler, label_encoders
