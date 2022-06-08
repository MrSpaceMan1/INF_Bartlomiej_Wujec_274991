import cv2 as cv
import numpy as np
from tensorflow import keras
import tensorflow as tf

model = keras.models.load_model('capitalLEttersConv')

img = cv.imread("z.png", cv.IMREAD_GRAYSCALE)

data = np.array(img)
data.reshape((28, 28, 1))
data = np.expand_dims(data, axis=2)
data = np.expand_dims(data, axis=0)

print(data.shape)
probability_model = tf.keras.Sequential([model, tf.keras.layers.Softmax()])

res = probability_model.predict(data)
print(res)


def classify(arr):
    max = arr[0]
    index = 0
    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
            index = i
    return index


nr = classify(res[0])

print(nr)
print(chr(ord("A") + nr))
