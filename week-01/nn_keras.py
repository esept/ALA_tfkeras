import tensorflow as tf
import numpy as np
from tensorflow import keras
from tensorflow.keras.layers import Dense

layer_1 = Dense(units=3,activation='sigmoid')
layer_2 = Dense(units=1,activation='sigmoid')
model1 = tf.keras.Sequential([layer_1,layer_2])

model = tf.keras.Sequential([
    Dense(units=3,activation='sigmoid'),
    Dense(units=1,activation='sigmoid')
])


x = np.array([[200.0,15.0],
              [120.0,5.0],
              [425.0,20.0],
              [212.0,18.0]])
x_new = np.array([[100.0,4.0]])
y = np.array([[1,0,0,1]])
print(layer_2)
# model = compile()
#
# model.fit(x,y)
#
# y_pre = model.predict(x_new)
# print(y_pre)
