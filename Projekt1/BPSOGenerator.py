from pyswarms.discrete.binary import BinaryPSO
from pyswarms.utils.plotters import plot_cost_history
import matplotlib.pyplot as plt
from mazeSolver import maze_solver, sum_neighbours, possible_moves, print_maze

maze_side = 10
options = {'c1': 0.5, 'c2': 0.3, 'w':0.9, 'k':2, 'p':1}


def fitness(solutions):
    score = 0
    for solution in solutions:

        if solution[0] == 0 and solution[maze_side**2-1] == 0:
            score += (maze_side**2)/2

        solvable, traversed = maze_solver(solution.tolist())

        if solvable:
            score += (maze_side**2)/2

        for i in range(0, maze_side**2):
            if solution[i] == 0:
                if sum_neighbours(i, solution) in (0, 1, 8):
                    score += -1
                if possible_moves(i, solution) == 0:
                    score += -2
            if solution[i] == 1:
                if sum_neighbours(i, solution) == 8:
                    score += -1

        empty_cells = int(maze_side**2 - sum(solution.tolist()))
        not_accessible = traversed-empty_cells
        score += not_accessible
    return -score


optimiser = BinaryPSO(100,
                      maze_side**2,
                      options=options)

best, solution = optimiser.optimize(fitness, iters=1000, verbose=True)
cost_history = optimiser.cost_history

print_maze(solution)
plot_cost_history(cost_history)
plt.show()
