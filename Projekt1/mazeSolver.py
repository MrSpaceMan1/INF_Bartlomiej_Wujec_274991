import math
import queue


def maze_solver(_maze: list):
    def pos_to_index(x, y):
        return x*maze_side + y

    def index_to_pos(index):
        return index//maze_side, index - (index//maze_side)*maze_side

    maze = _maze
    maze_side = int(math.sqrt(len(maze)))

    start = 0
    end = len(maze)-1

    to_visit = queue.SimpleQueue()
    visited = list()

    to_visit.put_nowait(start)
    while to_visit.qsize() != 0:
        index = to_visit.get_nowait()
        visited.append(index)
        if in_bounds(index-1, maze_side):
            to_visit.put_nowait(index-1)
        if in_bounds(index+1, maze_side):
            to_visit.put_nowait(index+1)
        if in_bounds(index+maze_side, maze_side):
            to_visit.put_nowait(index+maze_side)
        if in_bounds(index-maze_side, maze_side):
            to_visit.put_nowait(index-maze_side)

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
    return index >= 0 and index < maze_side**2


def sum_neighbours(index, maze):
    def pos_to_index(x, y):
        return x*maze_side + y

    def index_to_pos(index):
        return index//maze_side, index - (index//maze_side)*maze_side

    maze_side = int(math.sqrt(len(maze)))
    pos = index_to_pos(index)
    _sum = 0
    for i in range(-1, 1):
        for j in range(-1, 1):
            if in_bounds(pos_to_index(pos[0]+i, pos[1]+j), maze_side):
                _sum += maze[pos_to_index(pos[0]+i, pos[1]+j)]
    return _sum

def possible_moves(index, maze):
    def pos_to_index(x, y):
        return x*maze_side + y

    def index_to_pos(index):
        return index//maze_side, index - (index//maze_side)*maze_side

    maze_side = int(math.sqrt(len(maze)))
    x, y = index_to_pos(index)
    ways = 0
    for i in (-1, 1):
        if in_bounds(pos_to_index(x+i, y), maze_side):
            if maze[pos_to_index(x+i, y)] == 0:
                ways += 1
        if in_bounds(pos_to_index(x, y+i), maze_side):
            if maze[pos_to_index(x, y+i)] == 0:
                ways += 1
    return ways