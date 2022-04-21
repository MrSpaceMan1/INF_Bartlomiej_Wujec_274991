import math

from mazeSolver import maze_solver, walls_intact, sum_neighbours, possible_moves
import pygad

maze = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

maze_side = 10

def fitness(solution, solution_idx):
    score = 0
    if solution[0] == 0 and solution[maze_side**2-1] == 0:
        score+=10
    if maze_solver(solution):
        score+=10
    return score


gene_space = [0, 1]
fitness_func = fitness
sol_per_pop = 100
num_genes = maze_side**2
num_parents_mating = 10
num_generations = 300
keep_parents = 5
parent_selection_type = "sss"
crossover_type = "single_point"
mutation_type = "random"
mutation_percent_genes = int(num_genes*0.01)

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
                       mutation_percent_genes=mutation_percent_genes)

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