import copy, sys, time
from heapq import heappop, heappush

data = open("input.txt", "r").read().split('\n')

start = (0, 0, 0)
ex, ey = 0, 0
for i in range(len(data)):
    for q in range(len(data[0])):
        if data[i][q] == 'S':
            start = (i, q, 0)
        if data[i][q] == 'E':
            ex, ey = i, q

directions = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0)
]

def adjs(pos):
    (cx, cy, cd) = pos
    yield 1000, (cx, cy, (cd+1)%4)
    yield 1000, (cx, cy, (cd-1)%4)

    if cx+directions[cd][0] < len(data[0]) and cx+directions[cd][0] > -1 and cy+directions[cd][1] < len(data) and cy+directions[cd][1] > -1:
        if data[cx+directions[cd][0]][cy+directions[cd][1]] == '#':
            yield 1, (cx+directions[cd][0], cy+directions[cd][1], cd)

pq = []
dist = {}
for i in range(len(data)):
    for q in range(len(data[0])):
        dist[(i, q, 0)] = float("inf")
        dist[(i, q, 1)] = float("inf")
        dist[(i, q, 2)] = float("inf")
        dist[(i, q, 3)] = float("inf")

heappush(pq, (0, start))
while len(pq) > 0:
    dis, pos = heappop(pq)
    (cx, cy, cd) = pos
    if (cx, cy) == (ex, ey):
        print(dis)
        break
    for d, adj, in adjs(pos):
        if dis + d < dist[adj]:
            dist[adj] = dis+d
            heappush(pq, (dist[adj], adj))

print(dist)