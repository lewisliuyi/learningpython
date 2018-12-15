from __future__ import print_function


import keras
from keras. datasets import mnist
from keras.models import Sequential
from keras.layers import Dense,Dropout,Activation,Flatten
from keras.layers import Convolution2D,MaxPooling2D
from keras.utils import np_utils
from keras.optimizers import RMSprop

batch_size=128
num_classs=10
epochs=20
(x_train,y_train),(x_test,y_test)=mnist.load_data()

x_train=x_train.reshape(60000,784)
x_test=x_test.reshape(10000,784)
x_train=x_train.astype('float32')
x_test=x_test.astype('float32')