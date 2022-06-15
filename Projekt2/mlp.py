import numpy as np
from tensorflow.keras import datasets, layers, models
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

IMG_SIZE = 28

dataset: np.ndarray = np.loadtxt("./dataset.csv", delimiter=',', dtype=int)

train_set, test_set = train_test_split(dataset, train_size=0.8, random_state=274991)

train_x: np.ndarray = train_set[:, 1:].reshape((len(train_set), IMG_SIZE, IMG_SIZE, 1)) / 255.0
train_y: np.ndarray = train_set[:, 0].reshape((len(train_set), 1))

test_x = test_set[:, 1:].reshape((len(test_set), IMG_SIZE, IMG_SIZE, 1)) / 255.0
test_y = test_set[:, 0].reshape((len(test_set), 1))

train_y = to_categorical(train_y, 26)
test_y = to_categorical(test_y, 26)

mlp = models.Sequential([
    layers.Flatten(input_shape=(IMG_SIZE, IMG_SIZE, 1)),
    layers.Dense(256, activation="sigmoid"),
    layers.Dense(128, activation="sigmoid"),
    layers.Dense(26, activation="sigmoid")
])

mlp.summary()

mlp.compile(optimizer='adam',
            loss='categorical_crossentropy',
            metrics=['accuracy'])

history = mlp.fit(train_x, train_y, epochs=10)

plt.plot(history.history['accuracy'], label='accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.ylim([0.5, 1])
plt.legend(loc='lower right')

plt.show()

test_loss, test_acc = mlp.evaluate(test_x, test_y, verbose=2)
print(test_acc)

mlp.save("models.MLP")
