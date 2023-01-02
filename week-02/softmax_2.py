import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.losses import SparseCategoricalCrossentropy

if __name__ == '__main__':
    # Model
    model = Sequential([
        Dense(units=25, activation='relu'),
        Dense(units=15, activation='relu'),
        Dense(units=10, activation='linear')
    ])
    # loss
    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=1e-3),
        loss = SparseCategoricalCrossentropy(from_logits=True)
    )
    # fit
    model.fit(X,Y,epochs=100)
    #predict
    logits = model(X)
    f_x = tf.nn.softmax(logits)
    
