import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import pandas as pd

N = 100

k = 0.8
d = 1.3

x = np.random.random(N)
y = k*x + d + 0.01*np.random.randn(N)

res = stats.linregress(x,y)
print(res.intercept, res.slope)

#plt.plot(x,y,'ro')
#plt.show()

model = keras.Sequential([
    layers.Dense(4, activation=tf.nn.relu, input_shape=[1]),
    layers.Dense(4, activation=tf.nn.relu),
    layers.Dense(1)
  ])

optimizer = tf.keras.optimizers.RMSprop(0.001)

model.compile(loss='mean_squared_error',
              optimizer=optimizer,
              metrics=['mean_absolute_error', 'mean_squared_error'])



class PrintDot(keras.callbacks.Callback):
  def on_epoch_end(self, epoch, logs):
    if epoch % 100 == 0: print('')
    print('.', end='')

EPOCHS = 1000

early_stop = keras.callbacks.EarlyStopping(monitor='val_loss', patience=10)

history = model.fit(
  x, y,
  epochs=EPOCHS, validation_split = 0.2, verbose=0,
  callbacks=[early_stop, PrintDot()])

print("\n\n")

hist = pd.DataFrame(history.history)
hist['epoch'] = history.epoch
print(hist.tail())


xtrue = np.linspace(0,1,10)
ytrue = k*xtrue + d

xpred = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
ypred = model.predict(xpred).flatten()
ylinregpred = res.slope*np.array(xpred) + res.intercept
plt.plot(x,y,'rx', xpred,ypred,'go', xpred,ylinregpred,'ko', xtrue,ytrue,'-b')
plt.show()
#pred = model.predict(x).flatten()
#plt.plot(sorted(x), pred, '-rx')


