import numpy as np
import pandas as pd

df = pd.read_csv('./iris_with_errors.csv',
                 dtype={'sepal.length': float,
                        'sepal.width': float,
                        'petal.length': float,
                        'petal.width': float,
                        'variety': str},
                 na_values=['-', ' '])

print(df.isnull().sum())
print()

medians_df = df.median(0, skipna=True, numeric_only=True)

for name in ['sepal.length', 'sepal.width', 'petal.length', 'petal.width']:
    index = 0
    for i in df[name]:
        try:
            i = float(i)
            if 15 >= i <= 0:
                raise ValueError
        except ValueError:
            df.loc[index, name] = np.nan
        index += 1

index = 0
for i in df["variety"]:
    try:
        str(i)
    except ValueError:
        df.loc[index, "variety"] = np.nan
    index += 1

for name in ['sepal.length', 'sepal.width', 'petal.length', 'petal.width']:
    index = 0
    for i in df.isnull()[name]:
        if i:
            df.loc[index, name] = medians_df[name]
        index += 1

print(df.isnull().sum())

x = {
    'vir': 'virginica',
    'set': 'setosa',
    'ver': 'versicolor'
}

for i in range(150):
    df.loc[i, 'variety'] = df['variety'][i].lower()
    if df.loc[i, 'variety'] not in ['virginica', 'setosa', 'versicolor']:
        beginning = df['variety'][i][:3]
        try:
            df.loc[i, 'variety'] = x[beginning]
        except KeyError:
            df.drop(axis=0, index=i)


print(df)