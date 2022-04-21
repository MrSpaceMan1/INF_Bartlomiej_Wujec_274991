import math
import queue


def maze_solver(_maze: list, start=None, end=None):
    maze = _maze
    maze_side = int(math.sqrt(len(maze)))

    if start is None:
        start = 0
    if end is None:
        end = len(maze)-1

    to_visit = queue.Queue()
    visited = list()

    if maze[start] == 1:
        return False
    if maze[end] == 1:
        return False

    to_visit.put(start)
    while not to_visit.empty():
        index = to_visit.get()
        visited.append(index)

        if not in_first_column(index, maze_side):
            if (index-1) not in visited:
                if maze[index-1] == 0:
                    to_visit.put(index-1)

        if not in_last_column(index, maze_side):
            if (index+1) not in visited:
                if maze[index+1] == 0:
                    to_visit.put(index+1)

        if in_bounds(index+maze_side, maze_side):
            if (index + maze_side) not in visited:
                if maze[index+maze_side] == 0:
                    to_visit.put(index+maze_side)

        if in_bounds(index-maze_side, maze_side):
            if (index - maze_side) not in visited:
                if maze[index-maze_side] == 0:
                    to_visit.put(index-maze_side)

    return end in visited


def walls_intact(_maze: list):
    maze = _maze
    maze_side = int(math.sqrt(len(maze)))
    walls = 0
    intact = True
    for i in range(0, maze_side):
        if maze[i] != 1:
            intact = False
        else:
            walls+=1
    for i in range(maze_side, len(maze)-maze_side-1, maze_side):
        if maze[i] != 1:
            intact = False
        else:
            walls+=1
    for i in range(maze_side*2-1, len(maze)-maze_side-1, maze_side):
        if maze[i] != 1:
            intact = False
        else:
            walls+=1
    for i in range(maze_side*maze_side-maze_side-1, len(maze)):
        if maze[i] != 1:
            intact = False
        else:
            walls+=1
    return intact, walls


def in_bounds(index, maze_side):
    return 0 <= index < maze_side ** 2


def in_first_column(index, maze_side):
    return index % maze_side == 0


def in_last_column(index, maze_side):
    return (index+1) % maze_side == 0


def sum_neighbours(index, maze):
    maze_side = int(math.sqrt(len(maze)))
    _sum = 0

    if in_bounds(index - maze_side - 1, maze_side) and not in_first_column(index, maze_side):
        _sum += maze[index - maze_side - 1]

    if in_bounds(index - maze_side, maze_side):
        _sum += maze[index - maze_side]

    if in_bounds(index - maze_side + 1, maze_side) and not in_last_column(index, maze_side):
        _sum += maze[index - maze_side + 1]

    if not in_first_column(index, maze_side):
        _sum += maze[index - 1]

    if not in_last_column(index, maze_side):
        _sum += maze[index + 1]

    if in_bounds(index + maze_side - 1, maze_side) and not in_first_column(index, maze_side):
        _sum += maze[index + maze_side - 1]

    if in_bounds(index + maze_side, maze_side):
        _sum += maze[index + maze_side]

    if in_bounds(index + maze_side + 1, maze_side) and not in_last_column(index, maze_side):
        _sum += maze[index + maze_side + 1]

    return _sum


def possible_moves(index, maze):
    maze_side = int(math.sqrt(len(maze)))
    ways = 0

    if in_bounds(index-maze_side, maze_side):
        if maze[index-maze_side] == 0:
            ways += 1

    if in_bounds(index+maze_side, maze_side):
        if maze[index+maze_side] == 0:
            ways += 1

    if not in_first_column(index, maze_side):
        if maze[index-1] == 0:
            ways += 1

    if not in_last_column(index, maze_side):
        if maze[index+1] == 0:
            ways += 1
    return ways


def print_maze(maze: list, sides=True) -> None:
    maze_side = int(math.sqrt(len(maze)))
    if sides:
        for i in range(0, maze_side + 2):
            print("⬛", end="")
        print()

        print("⬛", end="")
    for i in range(0, len(maze)):
        if maze[i] == 1:
            print("⬛", end="")
        else:
            print("⬜", end="")
        if (i + 1) % maze_side == 0:
            if sides:
                print("⬛", end="")
                print()
                print("⬛", end="")
            else:
                print()
    if sides:
        for i in range(0, maze_side + 1):
            print("⬛", end="")
    print()


# maze = [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 1.0, 1.0, 0.0, 1.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 0.0]