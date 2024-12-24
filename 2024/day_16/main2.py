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

def adjs(pos):
    x, y, d = pos
    yield 1000, (x, y, (d+1)%4)
    yield 1000, (x, y, (d-1)%4)

    if x+directions[d][0] in range(len(data)) and y+directions[d][1] in range(len(data[0])) and data[x+directions[d][0]][y+directions[d][1]] != '#':
        yield 1, (x+directions[d][0], y+directions[d][1], d)

def adjs2(pos):
    x, y, d = pos
    yield 1000, (x, y, (d+1)%4)
    yield 1000, (x, y, (d-1)%4)
    yield 0, (x, y, (d+2)%4)

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

heappush(pq, (0, start))
dists[(start[0], start[1], 0)] = 0

best = None
while len(pq) > 0:
    dist, pos = heappop(pq)
    if (pos[0], pos[1]) == (end[0], end[1]) and best is None:
        best = dist
    for d, adj in adjs(pos):
        if dist + d < dists[adj]:
            dists[adj] = dist+d
            heappush(pq, (dists[adj], adj))

pq = []
for i in range(4):
    heappush(pq, (0, (end[0], end[1], i)))
    dists[(end[0], end[1], i)] = 0

dists2 = {}
for i in range(len(data)):
    for q in range(len(data[0])):
        if data[i][q] == '#':
            continue

        for d in range(len(directions)):
            dists2[(i, q, d)] = float("inf")

while len(pq) > 0:
    dist, pos = heappop(pq)
    if (pos[0], pos[1]) == (start[0], start[1]):
        pass
    for d, adj in adjs2(pos):
        if dist + d < dists2[adj]:
            dists2[adj] = dist+d
            heappush(pq, (dists2[adj], adj))


works = set()
for i in range(len(data)):
    for q in range(len(data[0])):
        for d in range(4):
            if (i, q, d) in dists and (i, q, d) in dists2 and dists[(i, q, d)] + dists2[(i, q, d)] == best:
                works.add((i, q))

print(len(works)+1)