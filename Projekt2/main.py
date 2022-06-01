import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

dataset = np.recfromtxt("./dataset.csv", delimiter=',', dtype=int)

train_set, test_set = train_test_split(dataset, train_size=0.8, random_state=274991)

train_inputs = train_set[:, 1:]
train_class = train_set[:, 0]
test_inputs = test_set[:, 1:]
test_class = test_set[:, 0]

classes = set()
for i in train_class:
    classes.add(i)

print(classes)