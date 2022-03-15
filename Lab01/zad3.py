from pandas import read_csv, concat, DataFrame
import matplotlib.pyplot as plt

miasta = read_csv("./miasta.csv")
print(miasta)

print(miasta.values)

miasta = concat([miasta,
                 DataFrame(
                     [[2010, 460, 555, 405]],
                     columns=["Rok", "Gdansk", "Poznan", "Szczecin"])]
                , ignore_index=True)
print(miasta)

plt.plot(miasta.loc[:, "Rok"], miasta.loc[:, "Gdansk"], marker='o', color="r")
plt.title('Ludność w miastach polski')
plt.ylabel("Ilość ludnosci")
plt.xlabel("Lata")
plt.show()

plt.plot(miasta.loc[:, "Rok"], miasta.loc[:, "Poznan"], marker='o', color="b")
plt.plot(miasta.loc[:, "Rok"], miasta.loc[:, "Szczecin"], marker="o", color="g")
plt.plot(miasta.loc[:, "Rok"], miasta.loc[:, "Gdansk"], marker='o', color="r")
plt.title('Ludność w miastach polski')
plt.ylabel("Ilość ludnosci")
plt.xlabel("Lata")
plt.show()
