import copy, sys, time
from heapq import heappush, heappop

data = open("input.txt", "r").read().split('\n')

start = (0, 0, 0)
end = (0, 0, 0)
for i in range(len(data)):
    for q in range(len(data[0])):
        if data[i][q] == 'S':
            start = (i, q, 0)
        if data[i][q] == 'E':
            end = (i, q, 0)

directions = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0)
]

print(data)
def adjs(pos):
    x, y, d = pos
    yield 1000, (x, y, (d+1)%4)
    yield 1000, (x, y, (d-1)%4)

    if x+directions[d][0] in range(len(data)) and y+directions[d][1] in range(len(data[0])) and data[x+directions[d][0]][y+directions[d][1]] != '#':
        yield 1, (x+directions[d][0], y+directions[d][1], d)


dists = {}
pq = []
for i in range(len(data)):
    for q in range(len(data[0])):
        if data[i][q] == '#':
            continue

        for d in range(len(directions)):
            dists[(i, q, d)] = float("inf")

pq = []
heappush(pq, (0, start))
dists[(start[0], start[1], 0)] = 0

while len(pq) > 0:
    dist, pos = heappop(pq)
    if (pos[0], pos[1]) == (end[0], end[1]):
        print(dist)
        break
    for d, adj in adjs(pos):
        if dist + d < dists[adj]:
            dists[adj] = dist+d
            heappush(pq, (dists[adj], adj))
