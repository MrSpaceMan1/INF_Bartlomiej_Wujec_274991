from tensorflow import keras
import numpy as np
from image_preprocessing import preprocess

symbols = preprocess("test.jpg", 500, 1500)
print(symbols.shape)

symbols = np.expand_dims(symbols, axis=3)

model = keras.models.load_model("models.CustomCNN")

res = model.predict(symbols)


def classify(arr):
    max = arr[0]
    index = 0
    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
            index = i
    return index


for r in res:
    print(chr(ord("A") + classify(r)), end="")
