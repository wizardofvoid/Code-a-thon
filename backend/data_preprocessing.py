import pandas as pd
from sklearn.preprocessing import StandardScaler
filepath="/Users/ivanpadeliya/Downloads"
def load_and_preprocess_data(filepath):
    # Load the data
    data = pd.read_csv(filepath)
    data = data.dropna()  # Remove missing values

    # Normalize the data
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data)

    # Convert scaled data back to DataFrame
    data_scaled = pd.DataFrame(data_scaled, columns=data.columns)
    
    return data_scaled, scaler
