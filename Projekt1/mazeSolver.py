import math

class Stack:
    def __init__(self):
        self.stack = []

    def add(self, val):
        self.stack.append(val)

    def pop(self):
        return_value = self.stack[-1]
        self.stack = self.stack[:-1]
        return return_value


def maze_solver(maze: list) -> bool:
    maze_side = int(math.sqrt(len(maze)))
    start = (1, 1)
    end = (maze_side-2, maze_side-2)

    stack = Stack()

    def pos_to_index(x, y):
        return x * maze_side + y

    def index_to_pos(index):
        return index//maze_side, index - (index//maze_side)*maze_side

    def empty_neighbours(x, y):
        sum = 0
        for i in (-1, 1):
            if maze[pos_to_index(x+i, y)] != 1:
                sum += 1
            if maze[pos_to_index(x, y+i)] != 1:
                sum += 1
        return sum

    # for i in range(0, len(maze)):
    #     maze[i] = "#" if maze[i] == 1 else 0

    for i in range(0, len(maze)):
        if maze[i] == 1:
            continue
        choices = empty_neighbours(*index_to_pos(i))
        maze[i] = choices if choices > 2 else 0

    for i in range(0, len(maze)):
        print(maze[i], end=" ")
        if (i + 1) % 5 == 0:
            print()

    pos = [*start]
    







maze = [1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1]

maze_solver(maze)
