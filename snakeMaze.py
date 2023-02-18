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
    print("possible moves from", point, "are:", new_moves)
    return new_moves

from time import sleep
def dfs(maze: List[List[str]], start: Tuple, goal: Tuple):
    # start by checking up, down, left, right of start
    agenda = []
    visited = set()
    visited.add(start)
    path = []
    for move in get_moves(start):
        if maze[move[0]][move[1]] == ' ':
            agenda.append(move)
            visited.add(move)
    current = agenda.pop()
    while current != goal:
        current = agenda.pop()
        # print(agenda, "current:", current)
        # print("visited:", visited)
        display_maze(maze, current)
        sleep(1)
        for move in get_moves(current):
            if (move == (5, 1)):
                print(agenda, visited, maze[1][5])
            if move not in visited and maze[move[1]][move[0]] == ' ':
                agenda.append(move)
                visited.add(move)



def main():
    display_maze(example_maze)
    snake, food = get_key_points(example_maze)
    dfs(example_maze, snake, food)

main()