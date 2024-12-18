import copy, sys
sys.setrecursionlimit(10000)

data = open("input.txt", "r").read().split('\n')

start = (0, 0)
for i in range(len(data)):
    for q in range(len(data[0])):
        if data[i][q] == 'S':
            start = (i, q)
            break


directions = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1)
    ]

explored_spaces = set()
smallest = 10000000000
def go(i, q, td, score, visited):
    global smallest
    global explored_spaces

    print(i, q)
    if (i, q) not in explored_spaces:
        explored_spaces.add((i, q))

    visited.add((i, q, td))
    if data[i][q] == 'E':
        smallest = min(smallest, score)
        return

    for d in directions:
        if data[i+d[0]][q+d[1]] != '#' and (i+d[0], q+d[1], d) not in visited:
            if d == td:
                go(i+d[0], q+d[1], d, score+1, copy.copy(visited))
            else:
                go(i+d[0], q+d[1], d, score+1001, copy.copy(visited))

go(start[0], start[1], (0, 1), 0, set())
print(smallest)