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
heappush(pq, (0, start))
dists = {}
for i in range(ex):
    for q in range(ey):
        dists[(i, q)] = float("inf")

dists[start] = 0
while len(pq) > 0:
    dist, pos = heappop(pq)
    if pos == (ex, ey):
        print(dist)
        break
    for d, adj in adjs(pos):
        if dist + d < dists[adj]:
            dists[adj] = dist+d
            heappush(pq, (dists[adj], adj))

print(dists[(ex, ey)])
