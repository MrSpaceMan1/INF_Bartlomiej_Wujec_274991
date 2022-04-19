import math

from mazeSolver import maze_solver, walls_intact, sum_neighbours, possible_moves
import pygad

maze = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

maze_side = 10

def fitness(solution, solution_idx):
    score = 0
    outside_walls_intact, number_of_walls = walls_intact(solution.tolist())

    if not outside_walls_intact:
        score += number_of_walls
    else:
        score += 6 * (4 * maze_side - 4)

        if solution[maze_side + 1] != 0:
            score += 3*(-maze_side*2-2)
        if solution[maze_side*maze_side - maze_side - 2]:
            score += 3*(-maze_side*2-2)
        #
        if not maze_solver(solution.tolist()):
            score += 3*(-maze_side*4)-4
        else:
            score += 3*(maze_side*4)-4
        #
        for i in range(0, maze_side**2):
            sum_of_neighbours = sum_neighbours(i, solution)
            sum_of_moves = possible_moves(i, solution)
            if solution[i] == 0 and sum_of_neighbours in (0, 8):
                score += -maze_side
            if solution[i] == 0 and sum_of_moves > 3:
                score += maze_side
            if solution[i] == 0 and sum_of_moves == 0:
                score += -maze_side
        #
        for i in range(0, maze_side**2, maze_side):
            sum_of_row = sum(solution[i:i+maze_side-1])
            if sum_of_row - 2 == 0:
                score += -3*maze_side
            if maze_side - 2 == sum_of_row:
                score += maze_side
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
                       mutation_percent_genes=mutation_percent_genes,
                       stop_criteria=["saturate_25"])

ga_instance.run()
solution, solution_fitness, solution_idx = ga_instance.best_solution()
a = solution.tolist()
print(solution_fitness)
for i in range(0, len(a)):
    if a[i] == 1:
        print("⬛", end="")
    else:
        print("⬜", end="")
    if (i+1) % int(math.sqrt(len(a))) == 0:
        print()
#
# ga_instance.plot_fitness()