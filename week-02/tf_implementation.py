import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.losses import BinaryCrossentropy
if __name__ == '__main__':
    model = Sequential([
        Dense(units=25,activation='sigmoid'),
        Dense(units=15,activation='sigmoid'),
        Dense(units=1,activation='sigmoid')
    ])
    model.compile(loss = BinaryCrossentropy())
    model.fit(X,Y,epochs=100)
    