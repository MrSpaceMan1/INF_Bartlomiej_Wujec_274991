import math
import time
from mazeSolver import maze_solver, sum_neighbours, possible_moves
import pygad


maze_side = 20
time_sum = 0
t1 = time.time()
t2 = None


def on_generation(instance):
    global cache_uses
    global time_sum
    global t1
    global t2
    t2 = time.time()
    time_sum += t2 - t1
    t1 = t2
    print(f"\n{instance.generations_completed} "
          f"| Time elapsed: {int(time_sum//60)}:{math.ceil(time_sum-((time_sum//60)*60))} "
          f"| Generation fitness: {instance.best_solutions_fitness[-1]} ")


def fitness(solution, solution_idx):
    # global cache
    # global cache_uses
    # if cache.get(array2string(solution)) is not None:
    #     cache_uses += 1
    #     return cache[array2string(solution)]

    score = 0
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
    # if cache.get(array2string(solution)) is None:
    #     cache[array2string(solution)] = score
    return score


gene_space = [0, 1]
fitness_func = fitness
sol_per_pop = 200
num_genes = maze_side**2
num_parents_mating = 20
num_generations = 300
keep_parents = 10
parent_selection_type = "sss"
crossover_type = "single_point"
mutation_type = "random"
mutation_percent_genes = math.ceil(num_genes*0.03)

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
                       stop_criteria=["saturate_50"]
                       )

# ga_instance.run()
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
