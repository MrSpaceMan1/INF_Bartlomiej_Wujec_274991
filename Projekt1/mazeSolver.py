import math
import queue


def maze_solver(_maze: list):
    def pos_to_index(x, y):
        return x*maze_side + y

    def index_to_pos(index):
        return index//maze_side, index - (index//maze_side)*maze_side

    maze = _maze
    maze_side = int(math.sqrt(len(maze)))
    to_visit = queue.SimpleQueue()
    visited = list()
    to_visit.put_nowait(pos_to_index(1, 1))
    while to_visit.qsize() != 0:
        curr_node = index_to_pos(to_visit.get_nowait())
        visited.append(pos_to_index(*curr_node))
        maze[pos_to_index(*curr_node)] = 2
        try:
            for i in (-1, 1):
                if maze[pos_to_index(curr_node[0]+i, curr_node[1])] == 0:
                    if pos_to_index(curr_node[0]+i, curr_node[1]) not in visited:
                        to_visit.put_nowait(pos_to_index(curr_node[0]+i, curr_node[1]))
                if maze[pos_to_index(curr_node[0], curr_node[1]+i)] == 0:
                    if pos_to_index(curr_node[0], curr_node[1]+i) not in visited:
                        to_visit.put_nowait(pos_to_index(curr_node[0], curr_node[1]+i))
        except IndexError as e:
            print(curr_node)
            print(visited)
            print(to_visit)
            print("MAJOR FUCK UP, FIX THIS SHIT")
            return False
        if curr_node == (maze_side-2, maze_side-2):
            break
    return pos_to_index(*(maze_side-2, maze_side-2)) in visited


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