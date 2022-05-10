import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("iris.csv")
(train_set, test_set) = train_test_split(df.values, train_size=0.7, random_state=274991)

train_inputs = train_set[:, 0:4]
train_classes = train_set[:, 4]
test_inputs = test_set[:, 0:4]
test_classes = test_set[:, 4]

def classify_iris(sl, sw, pl, pw):
    if sl < 5.8:
        return("setosa")
    elif pl > 5:
        return("virginica")
    else:
        return("versicolor")

correct = 0
for i in test_set:
    if classify_iris(*i[:4]) == i[-1]:
        correct += 1
print(correct / len(test_set))

