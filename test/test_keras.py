
from __future__ import absolute_import, division, print_function, unicode_literals
import os
os.environ["KMP_DUPLICATE_LTB_OK"]='True'
import tensorflow as tf
from tensorflow import keras

import numpy as np
import matplotlib.pyplot as plt

print(tf.__version__) # 1.13.1

def minst():
    # 下载mnist数据
    fashion_mnist = keras.datasets.fashion_mnist
    (train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()


    class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
                   'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

    print(train_images.shape) # (60000, 28, 28)
    print(train_labels) # [9 0 0 ... 3 0 5]


    # 预处理图片数据
    plt.figure()
    plt.imshow(train_images[0])
    plt.colorbar()
    plt.grid(False)
    plt.show()

    train_images = train_images / 255.0
    test_images = test_images / 255.0


    plt.figure(figsize=(10, 10))
    for i in range(25):
        plt.subplot(5, 5, i+1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(train_images[i], cmap=plt.cm.binary)
        plt.xlabel(class_names[train_labels[i]])
    plt.show()

    model = keras.Sequential([
        keras.layers.Flatten(input_shape=(28, 28)),
        keras.layers.Dense(128, activation='relu'),
        keras.layers.Dense(10, activation='softmax')
    ])

    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=["accuracy"])

    model.fit(train_images, train_labels, epochs=10)

from keras.layers import Input, Dense
from keras.models import Model

# 全连接神经网络
def dense_model():
    inputs = Input(shape=(784,))
    x = Dense(64, activation='relu')(inputs)
    y = Dense(64, activation='relu')(x)
    predictions = Dense(10, activation='softmax')(x)
    print(inputs)
    print("x", x)

    # 创建包含输入层和三个全连接层的模型
    model = Model(inputs=inputs, outputs=predictions)
    model.compile(optimizer='rmsprop',
                  loss='categorical_crossentrop',
                  metrics=['accuracy'])

from keras import backend as K
from keras.layers import Input, Lambda
def test_mask():
    x = [0, 1, 2]
    x_mask = Lambda(lambda x: K.cast(K.greater(K.expand_dims(x, 2), 0), 'float32'))(x)
    print(x_mask)

if __name__ == '__main__':
    # dense_model()
    test_mask()