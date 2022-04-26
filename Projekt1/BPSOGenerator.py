import numpy
from pyswarms.discrete.binary import BinaryPSO
from pyswarms.utils.plotters import plot_cost_history
import time
import matplotlib.pyplot as plt
from mazeSolver import maze_solver, sum_neighbours, possible_moves, print_maze

maze_side = 20
options = {'c1': 0.5, 'c2': 0.3, 'w':0.9, 'k':2, 'p':1}


def fitness(solution):
    score = 0
    if solution[0] == 0 and solution[maze_side ** 2 - 1] == 0:
        score += (maze_side ** 2) / 2

    solvable, traversed = maze_solver(solution.tolist())

    if solvable:
        score += (maze_side ** 2) / 2

    for i in range(0, maze_side ** 2):
        if solution[i] == 0:
            if sum_neighbours(i, solution) in (0, 1, 2, 7, 8):
                score += -2
            if possible_moves(i, solution) == 0:
                score += -2
        if solution[i] == 1:
            if sum_neighbours(i, solution) > 4:
                score += -1
    row_sum = 0

    for i in range(0, maze_side ** 2):
        row_sum += solution[i]
        if (i + 1) % maze_side == 0:
            if row_sum > maze_side / 1.5:
                score += -8

    empty_cells = int(maze_side ** 2 - sum(solution.tolist()))
    not_accessible = traversed - empty_cells
    score += not_accessible
    return -score


def f(x):
    num_of_particles = x.shape[0]
    j = [fitness(x[i]) for i in range(0, num_of_particles)]
    return numpy.array(j)


optimiser = None
time_sum = 0
for i in range(0, 10):
    t1 = time.time()

    optimiser = BinaryPSO(30,
                          maze_side ** 2,
                          options=options,
                          velocity_clamp=(-6, 6))

    best, solution = optimiser.optimize(f, iters=1000, verbose=True)

    t2 = time.time()
    time_sum += t2 - t1
print(time_sum/10)
cost_history = optimiser.cost_history

# print_maze(solution)
plot_cost_history(cost_history)
plt.show()
