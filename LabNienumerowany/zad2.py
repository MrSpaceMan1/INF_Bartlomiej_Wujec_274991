import pandas as pd
import numpy as np
from mlxtend.frequent_patterns import apriori, association_rules
import matplotlib.pyplot as plt

df = pd.read_csv("titanic.csv", sep=",", usecols=[1, 2, 3, 4])

prepared_df = pd.DataFrame(
    np.zeros((len(df), 7)),
    index=range(len(df)),
    columns=["3rd", "2nd", "1st", "Crew", "Sex", "Age", "Survived"])

cls = {
    "3rd": 0,
    "2nd": 1,
    "1st": 2,
    "Crew": 3
}

sex = {
    "Male": 0.0,
    "Female": 1.0
}

age = {
    "Adult": 0.0,
    "Child": 1.0
}

survived = {
    "No": 0.0,
    "Yes": 1.0
}

for i in range(len(df)):
    x = df[0+i:1+i].values[0]
    vals = [0.0 for i in range(7)]
    vals[cls[x[0]]] = 1.0
    vals[4] = sex[x[1]]
    vals[5] = age[x[2]]
    vals[6] = survived[x[3]]
    prepared_df[0+i:1+i] = vals

freq_items = apriori(prepared_df, min_support=0.01, use_colnames=True, verbose=1)
print(freq_items.head(7))

rules = association_rules(freq_items, metric='confidence', min_threshold=0.8, support_only=False)
for i in range(3):
    print(rules.loc[i])
    print()

# Z zasad:
# Przeżywały kobiety z drugiej klasy
# Przeżywały dzieci z drugiej klasy
# Przeżywały kobiety z pierwszej klasy
#
#