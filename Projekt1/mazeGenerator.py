from mazeSolver import maze_solver, walls_intact, sum_neighbours, possible_moves
import pygad

maze = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

maze_side = 20

def fitness(solution, solution_idx):
    score = 0
    outside_walls_intact, number_of_walls = walls_intact(solution.tolist())
    if not outside_walls_intact:
        return number_of_walls
    else:
        score += 1000

    if not maze_solver(solution.tolist()):
        return number_of_walls
    else:
        score += 1000

    if solution[maze_side + 1] != 0:
        score += -500
    if solution[maze_side*maze_side - maze_side - 2]:
        score += -500

    for i in range(0, maze_side**2):
        sum_of_neighbours = sum_neighbours(i, solution)
        sum_of_moves = possible_moves(i, solution)
        if solution[i] == 0 and sum_of_neighbours == 8:
            score += -50
        if solution[i] == 0 and sum_of_neighbours == 0:
            score += -50
        if solution[i] == 0 and sum_of_moves > 3:
            score += 5
        if solution[i] == 0 and sum_of_moves == 0:
            score += -100

    for i in range(0, maze_side**2, maze_side):
        sum_of_row = sum(solution[i:i+maze_side-1])
        if sum_of_row - 2 == 0:
            score += -20
        if sum_of_row - 2 == maze_side - 4:
            score += -20
    return score


gene_space = [0, 1]
fitness_func = fitness
sol_per_pop = 100
num_genes = maze_side**2
num_parents_mating = 10
num_generations = 1000
keep_parents = 10
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
for i in range(0, len(a)):
    if a[i] == 1:
        print("⬛", end="")
    else:
        print("⬜", end="")
    if (i+1) % maze_side == 0:
        print()

ga_instance.plot_fitness()