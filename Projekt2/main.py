import random

import keras
import numpy as np
from tensorflow.keras import datasets, layers, models
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import tensorflow as tf

IMG_SIZE = 28

dataset: np.ndarray = np.loadtxt("./dataset.csv", delimiter=',', dtype=int)

print(dataset.shape)

train_set, test_set = train_test_split(dataset, train_size=0.8, random_state=274991)

train_inputs: np.ndarray = train_set[:, 1:].reshape((len(train_set), IMG_SIZE, IMG_SIZE, 1)) / 255.0
train_class: np.ndarray = train_set[:, 0].reshape((len(train_set), 1))

test_inputs = test_set[:, 1:].reshape((len(test_set), IMG_SIZE, IMG_SIZE, 1)) / 255.0
test_class = test_set[:, 0].reshape((len(test_set), 1))

train_class = to_categorical(train_class, 26)
test_class = to_categorical(test_class, 26)

model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation="relu", input_shape=(IMG_SIZE, IMG_SIZE, 1)))
model.add(layers.AveragePooling2D((2, 2)))
# model.add(layers.Conv2D(64, (3, 3), activation='relu'))
# model.add(layers.AveragePooling2D((2, 2)))

# model.add(layers.Conv2D(128, (3, 3), activation='relu'))
#
model.add(layers.Flatten())
model.add(layers.Dense(1024, activation="relu"))
model.add(layers.Dropout(0.2))
model.add(layers.Dense(26, activation="softmax"))

model.summary()

model.compile(optimizer='adam',
              loss="categorical_crossentropy",
              metrics=['accuracy'])

history = model.fit(train_inputs, train_class, epochs=10, validation_split=0.15)

plt.plot(history.history['accuracy'], label='accuracy')
plt.plot(history.history['val_accuracy'], label='val_accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.ylim([0.5, 1])
plt.legend(loc='lower right')

plt.show()

test_loss, test_acc = model.evaluate(test_inputs, test_class, verbose=2)

model: keras.Model

model.save("capitalLettersConv")

probability_model = tf.keras.Sequential([model, tf.keras.layers.Softmax()])

res = probability_model.predict(test_inputs)

print(test_acc)
