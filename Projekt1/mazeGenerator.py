import math
import time
from mazeSolver import maze_solver, walls_intact, sum_neighbours, possible_moves
import pygad

maze = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

cache = {

}

maze_side = 20
time_sum = 0
t1 = time.time()
t2 = None
def on_generation(instance):
    global time_sum
    global t1
    global t2
    t2 = time.time()
    time_sum += t2 - t1
    t1 = t2
    print(f"{instance.generations_completed} | Time elapsed: {int(time_sum//60)}:{math.ceil(time_sum-((time_sum//60)*60))}")

def fitness(solution, solution_idx):
    global cache
    if cache[solution.array2string()]:
        return cache[solution.array2string()]
    score = 0
    if solution[0] == 0 and solution[maze_side**2-1] == 0:
        score+=10

    solvable, traversed = maze_solver(solution)

    if solvable:
        score+=10

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
    if not cache[solution.array2string()]:
        cache[solution.array2string()] = score
    return score


gene_space = [0, 1]
fitness_func = fitness
sol_per_pop = 100
num_genes = maze_side**2
num_parents_mating = 10
num_generations = 100
keep_parents = 5
parent_selection_type = "sss"
crossover_type = "single_point"
mutation_type = "random"
mutation_percent_genes = math.ceil(num_genes*0.01)

ga_instance = pygad.GA(gene_space=gene_space,
                       num_generations=num_generations,
                       num_parents_mating=num_parents_mating,
                       fitness_func=fitness_func,
                       sol_per_pop=sol_per_pop,
                       num_genes=num_genes,
                       parent_selection_type=parent_selection_type,
                       keep_parents=keep_parents,
                       crossover_type=crossover_type,
                       mutation_type=mutation_type,
                       mutation_percent_genes=mutation_percent_genes,
                       on_generation=on_generation,
                       # stop_criteria=["saturate_30"]
                       )

ga_instance.run()
solution, solution_fitness, solution_idx = ga_instance.best_solution()
a = solution.tolist()
print(solution_fitness)
for i in range(0, maze_side+2):
    print("⬛", end="")
print()
print("⬛", end="")
for i in range(0, len(a)):
    if a[i] == 1:
        print("⬛", end="")
    else:
        print("⬜", end="")
    if (i+1) % int(math.sqrt(len(a))) == 0:
        print("⬛", end="")
        print()
        print("⬛", end="")
for i in range(0, maze_side+1):
    print("⬛", end="")
print()

ga_instance.plot_fitness()