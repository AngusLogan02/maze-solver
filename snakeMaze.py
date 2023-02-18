from typing import List, Tuple

example_maze =  [['+', '-', '+', '-', '+', '-', '+'],
                 ['|', ' ', ' ', ' ', ' ', ' ', '|'],
                 ['+', ' ', '+', '-', '+', ' ', '+'],
                 ['|', ' ', ' ', 'F', '|', ' ', '|'],
                 ['+', '-', '+', '-', '+', ' ', '+'],
                 ['|', '$', ' ', ' ', ' ', ' ', '|'],
                 ['+', '-', '+', '-', '+', '-', '+']]

def display_maze(maze: List[List[str]], highlight: Tuple = (999, 999)):
    for y, line in enumerate(maze):
        for x, char in enumerate(line):
            if x == highlight[0] and y == highlight[1]:
                print('x', end='')
            else:
                print(char, end='')
        print()
    print("#####################")

def get_key_points(maze: List[List[str]]):
    for y, line in enumerate(maze):
        for x, char in enumerate(line):
            if char == '$':
                snake = (x, y)
            if char == 'F':
                food = (x, y)

    return snake, food

def get_moves(point: Tuple):
    x = point[0]
    y = point[1]
    new_moves = [(x, y+1), (x+1, y), (x, y-1), (x-1, y)]
    return new_moves

def get_char(maze: List[List[str]], point: Tuple):
    return maze[point[1]][point[0]]

def get_directions(one: Tuple, two: Tuple):
    x_diff = two[0] - one[0]
    y_diff = two[1] - one[1]

    if x_diff < 0:
        return "left"
    elif x_diff > 0:
        return "right"
    elif y_diff < 0:
        return "up"
    else:
        return "down"
    
def directions_list(solution: List[Tuple]):
    dir_list = []
    for i in range(0, len(solution)-1):
        dir_list.append(get_directions(solution[i], solution[i+1]))
    return dir_list

from time import sleep
def dfs(maze: List[List[str]], start: Tuple, goal: Tuple):
    # start by checking up, down, left, right of start
    agenda = []
    visited = set()
    visited.add(start)
    parents = {start: None}
    path = []
    for move in get_moves(start):
        if get_char(maze, move) == ' ':
            agenda.append(move)
            visited.add(move)
            parents[move] = start
    while agenda:
        current = agenda.pop()
        display_maze(maze, current)
        for move in get_moves(current):
            if(move == goal):
                    path.append(current)
                    while True:
                        current = parents[current]
                        if current == None:
                            path.insert(0, goal)
                            return path[::-1]
                        path.append(current)
                    
            if move not in visited and get_char(maze, move) == ' ':
                parents[move] = current
                agenda.append(move)
                visited.add(move)
            
    return None



def main(maze: List[List[str]]):
    snake, food = get_key_points(maze)
    solution = dfs(maze, snake, food)
    if solution is None:
        print("No solution available")
        return
    dirs = directions_list(solution)
    print(dirs)

main(example_maze)