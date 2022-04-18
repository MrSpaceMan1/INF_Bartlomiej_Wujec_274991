import pyswarms as ps
from pyswarms.utils.functions import single_obj as fx
options = {'c1': 0.5, 'c2': 0.3, 'w':0.9}
optimizer = ps.single.GlobalBestPSO(n_particles=10, dimensions=2,
options=options)
optimizer.optimize(fx.sphere, iters=1000)

# import pyswarms as ps
# from pyswarms.utils.functions import single_obj as fx