import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

df = pd.read_csv('./iris.csv')

def data_lost(original, reduced):
    u = 0
    d = 0
    for name in filter(lambda x: x!='class', original.columns):
        d += original[name].var()
    for name in filter(lambda x: x!='class', reduced.columns):
        u += reduced[name].var()
    return 1 - (u/d)

features = ["sepallength", "sepalwidth", "petallength", "petalwidth"]

# Separating out the features
x = df.loc[:, features].values  # Separating out the target
y = df.loc[:, ['class']].values  # Standardizing the features
x = StandardScaler().fit_transform(x)

from sklearn.decomposition import PCA

pca = PCA(n_components=2)
principalComponents = pca.fit_transform(x)
principalDf = pd.DataFrame(data=principalComponents)

finalDf = pd.concat([principalDf, df[['class']]], axis=1)
print(finalDf)
print(data_lost(df, finalDf))

colors = {
    "setosa": 0,
    "virginica": 1,
    "versicolor": 2
}

fig, ax = plt.subplots()
ax.scatter(finalDf[0], finalDf[1], c=list(map(lambda x: colors[x], finalDf['class'])))
ax.legend()

plt.show()