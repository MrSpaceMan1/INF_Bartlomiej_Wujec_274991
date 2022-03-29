import pygad
import numpy
import time


def is_wall(pos: tuple):
    return maze[pos[0]][pos[1]] == 1


def navigate(steps: list) -> tuple:
    #      Y  X
    pos = [1, 1]
    for step in steps:
        if step == 0:
            if not is_wall((pos[0]-1, pos[1])):
                pos[0] -= 1
        if step == 1:
            if not is_wall((pos[0], pos[1]+1)):
                pos[1] += 1
        if step == 2:
            if not is_wall((pos[0]+1, pos[1])):
                pos[0] += 1
        if step == 3:
            if not is_wall((pos[0], pos[1]-1)):
                pos[0] -= 1
        if pos[0] == 11 and pos[1] == 1:
            break
    return pos[0], pos[1]

def solve(steps: list) -> list:
    maze = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 2, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
            [1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1],
            [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1],
            [1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1],
            [1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1],
            [1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1],
            [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
    pos = [1, 1]
    for step in steps:
        if step == 0:
            if not is_wall((pos[0]-1, pos[1])):
                pos[0] -= 1
        if step == 1:
            if not is_wall((pos[0], pos[1]+1)):
                pos[1] += 1
        if step == 2:
            if not is_wall((pos[0]+1, pos[1])):
                pos[0] += 1
        if step == 3:
            if not is_wall((pos[0], pos[1]-1)):
                pos[0] -= 1
        maze[pos[0]][pos[1]] = 2
        if pos[0] == 11 and pos[1] == 1:
            break
    return maze


maze = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1],
        [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1],
        [1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1],
        [1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1],
        [1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1],
        [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# 0-UP 1-RIGHT 2-DOWN 3-LEFT
gene_space = [0, 1, 2, 3]

#definiujemy funkcję fitness
def fitness_func(solution, solution_idx):
    end = navigate(solution)
    distance = abs(end[0] - 10) + abs(end[1] - 10)
    return -distance

fitness_function = fitness_func

#ile chromsomów w populacji
#ile genow ma chromosom
sol_per_pop = 100
num_genes = 30

#ile wylaniamy rodzicow do "rozmanazania" (okolo 50% populacji)
#ile pokolen
#ilu rodzicow zachowac (kilka procent)
num_parents_mating = 10
num_generations = 100
keep_parents = 2

#jaki typ selekcji rodzicow?
#sss = steady, rws=roulette, rank = rankingowa, tournament = turniejowa
parent_selection_type = "sss"

#w il =u punktach robic krzyzowanie?
crossover_type = "single_point"

#mutacja ma dzialac na ilu procent genow?
#trzeba pamietac ile genow ma chromosom
mutation_type = "random"
mutation_percent_genes = 4

#inicjacja algorytmu z powyzszymi parametrami wpisanymi w atrybuty
time_sum = 0
t1 = 0
t2 = 0
ga_instance = None
for i in range(0, 10):
    t1 = time.time()
    ga_instance = pygad.GA(gene_space=gene_space,
                           num_generations=num_generations,
                           num_parents_mating=num_parents_mating,
                           fitness_func=fitness_function,
                           sol_per_pop=sol_per_pop,
                           num_genes=num_genes,
                           parent_selection_type=parent_selection_type,
                           keep_parents=keep_parents,
                           crossover_type=crossover_type,
                           mutation_type=mutation_type,
                           mutation_percent_genes=mutation_percent_genes,
                           stop_criteria=["reach_0"])

    #uruchomienie algorytmu
    ga_instance.run()
    t2 = time.time()
    time_sum += (t2 - t1)

#podsumowanie: najlepsze znalezione rozwiazanie (chromosom+ocena)
solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Parameters of the best solution : {solution}".format(solution=solution))
print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))
solved = solve(solution)

for row in solved:
    print(row)

print(time_sum/10)
#wyswietlenie wykresu: jak zmieniala sie ocena na przestrzeni pokolen
ga_instance.plot_fitness()