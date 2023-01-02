import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.losses import SparseCategoricalCrossentropy

if __name__ == '__main__':
    model = Sequential([
        Dense(units=25, activation='relu'),
        Dense(units=15, activation='relu'),
        Dense(units=10, activation='softmax')
    ])
    
    model.compile(loss = SparseCategoricalCrossentropy())
    
    model.fit(X,Y,epochs=100)
