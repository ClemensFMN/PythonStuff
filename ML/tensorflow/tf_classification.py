import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import pandas as pd

N = 10
sw2 = 0.1


mean1 = np.random.random(2)
mean2 = np.random.random(2)

p1 = np.zeros((2,N))
p2 = np.zeros((2,N))

for i in range(N):
  p1[:,i] = mean1 + sw2*np.random.randn(2)
  p2[:,i] = mean2 + sw2*np.random.randn(2)


plt.plot(p1[0,:], p1[1,:],'rx')
plt.plot(mean1[0], mean1[1],'ro')
plt.plot(p2[0,:], p2[1,:],'bx')
plt.plot(mean2[0], mean2[1],'bo')
plt.show()

model = keras.Sequential([
    layers.Dense(4, activation=tf.nn.relu, input_shape=[20]),
    layers.Dense(4, activation=tf.nn.softmax),
    layers.Dense(1)
  ])


model.compile(optimizer='adam', 
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])


all_points = np.hstack((p1,p2))
all_labels = [1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2]

model.fit(all_points, all_labels, epochs=5)


