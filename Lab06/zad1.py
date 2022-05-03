import numpy as np

db = np.genfromtxt("./iris_with_errors.csv",
                   encoding="utf",
                   delimiter=',',
                   names=['slength', 'swidth', 'plength', 'pwidth', 'variety'],
                   dtype=np.dtype([('slength', 'float'),
                                   ('swidth', 'float'),
                                   ('plength', 'float'),
                                   ('pwidth', 'float'),
                                   ('variety', 'S20')]))
db = np.array(db.tolist())
print(db)
db[:, 4] = [db[i, 4].lower() for i in range(db.shape[0])]
print(db)