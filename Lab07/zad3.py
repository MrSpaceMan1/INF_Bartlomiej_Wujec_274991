import pandas as pd
from sklearn.model_selection import train_test_split
import sklearn.tree as tree

df = pd.read_csv("iris.csv")

(train_set, test_set) = train_test_split(df.values, train_size=0.7, random_state=274991)

train_inputs = train_set[:, 0:4]
train_classes = train_set[:, 4]
test_inputs = test_set[:, 0:4]
test_classes = test_set[:, 4]

clf = tree.DecisionTreeClassifier()
clf.fit(train_inputs, train_classes)
correct = -0
for i in test_set:
    if clf.predict([i[:4]])[0] == i[4]:
        correct += 1

print(correct / len(test_set))
tree.plot_tree(clf)