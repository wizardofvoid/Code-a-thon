from model import build_autoencoder
from sklearn.model_selection import train_test_split

def train_model(data, save_path='unsupervised_anomaly_detection_model.h5'):
    # Split data into training and testing
    train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)

    # Build the model
    autoencoder = build_autoencoder(input_dim=train_data.shape[1])

    # Train the model
    autoencoder.fit(train_data, train_data, 
                    epochs=50, 
                    batch_size=32, 
                    shuffle=True, 
                    validation_split=0.2, 
                    verbose=1)
    
    # Save the trained model
    autoencoder.save(save_path)
    
    return autoencoder, test_data
