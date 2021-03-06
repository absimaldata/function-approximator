import keras
from keras.layers import Activation
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout, BatchNormalization, concatenate
from keras.initializers import RandomNormal
from keras.initializers import Zeros
from keras.optimizers import Adam, SGD, RMSprop
from keras.utils.generic_utils import get_custom_objects
from keras import Model
import keras.backend as K
import tensorflow as tf
import math
import numpy as np
import random

x = np.array([[1.0, 1.0]])
logx = np.array([[0.0, 0.0]])
y = np.array([1.0])
for i in range(10000):
  r1 = random.uniform(1,99)
  r2 = random.uniform(1,99)
  m1 = min(r1,r2)
  m2 = max(r1, r2)
  x = np.append(x, [[m1, m2]], axis=0)
  logx = np.append(logx, [[math.log(m1), math.log(m2)]], axis=0)
  y = np.append(y, [3 * m1 * m1 * m1 +  2 * m2 * m1 + 4* m2])

opt = Adam(learning_rate=0.01, clipnorm=1)
initializer = tf.keras.initializers.GlorotUniform()

logInput = keras.Input(shape=(2,), name="logInput")

logDense = Dense(10, kernel_initializer=initializer, activation='linear')(logInput)
logDense = Dense(10, kernel_initializer=initializer, activation='linear')(logDense)
logDense = Dense(10, kernel_initializer=initializer, activation='exponential')(logDense)
finalDense = Dense(10, kernel_initializer=initializer, activation='linear')(logDense)
finalDense = Dense(10, kernel_initializer=initializer, activation='linear')(logDense)
finalDense = Dense(1, kernel_initializer=initializer, activation='linear')(finalDense)
model = Model(inputs=[logInput], outputs=[finalDense])

model.summary()
model.compile(loss=tf.keras.losses.MeanAbsolutePercentageError(), optimizer=opt)
model.fit(logx, y, epochs=50)
opt.learning_rate.assign(0.001)
model.fit(logx, y, initial_epoch=50, epochs=100, batch_size=16)
opt.learning_rate.assign(0.0001)
model.fit(logx, y, initial_epoch=100, epochs=150, batch_size=32)
opt.learning_rate.assign(0.0001)
model.fit(logx, y, initial_epoch=150, epochs=200, batch_size=32)
opt.learning_rate.assign(0.0001)
model.fit(logx, y, initial_epoch=200, epochs=250, batch_size=32)
opt.learning_rate.assign(0.00001)
model.fit(logx, y, initial_epoch=250, epochs=300, batch_size=32)

#opt.learning_rate.assign(0.00001)
#model.fit(x, y, initial_epoch=300, epochs=400, batch_size=10)
sample1 = np.array([[3.0, 4.0], [12.0, 11.0], [111.0, 111.0]])
sample2 = np.array([[math.log(3), math.log(4)], [math.log(12), math.log(11)], [math.log(111), math.log(111)]])
print(model.predict(sample2))
