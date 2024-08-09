import tensorflow as tf

def build_autoencoder(input_dim):
    # Encoder
    input_layer = tf.keras.Input(shape=(input_dim,))
    encoder = tf.keras.layers.Dense(16, activation="relu")(input_layer)
    encoder = tf.keras.layers.Dense(8, activation="relu")(encoder)

    # Decoder
    decoder = tf.keras.layers.Dense(16, activation="relu")(encoder)
    decoder = tf.keras.layers.Dense(input_dim, activation="sigmoid")(decoder)

    # Autoencoder model
    autoencoder = tf.keras.Model(inputs=input_layer, outputs=decoder)
    autoencoder.compile(optimizer='adam', loss='mean_squared_error')
    
    return autoencoder
