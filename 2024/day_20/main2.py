from heapq import heappush, heappop
import copy, sys
import time


fl = open("input.txt", "r")
s = fl.read().split('\n')
fl.close()


start = (0, 0)
end = (0, 0)
mp = {}
for i in range(len(s)):
    for q in range(len(s)):
        if s[i][q] == 'S':
            start = (i, q)
        if s[i][q] == 'E':
            end = (i, q)
        if s[i][q] == '#':
            mp[(i, q)] = True

dists = {}
prev = {}
def go(data):
    def adjs(pos):
        i, q = pos
        if i-1 > -1 and (i-1, q) not in mp:
            yield 1, (i-1, q)
        if i+1 < len(data) and (i+1, q) not in mp:
            yield 1, (i+1, q)
        if q-1 > -1 and (i, q-1) not in mp:
            yield 1, (i, q-1)
        if q+1 < len(data) and (i, q+1) not in mp:
            yield 1, (i, q+1)


    pq = []
    heappush(pq, (0, start))

    for i in range(len(data)):
        for q in range(len(data)):
            prev[(i, q)] = None
            dists[(i, q)] = float("inf")

    dists[start] = 0
    while len(pq) > 0:
        dist, pos = heappop(pq)
        if pos == (end[0], end[1]):
            return dist, prev
            break
        for d, adj in adjs(pos):
            if dist + d < dists[adj]:
                dists[adj] = dist+d
                prev[adj] = pos
                heappush(pq, (dists[adj], adj))

    return None


path = set()
def trace(start, end):
    path.add(end)
    while end != start:
        end = prev[end]
        if end == None:
            return
        path.add(end)

dist = go(s)
trace(start, end)

cheats = set()
for i in path:
    x1, y1 = i
    for q in path:
        x2, y2 = q
        if abs(x2-x1) + abs(y2-y1) <= 20 and (dists[i]-dists[q])-(abs(x2-x1) + abs(y2-y1)) >= 100:
            if (q, i) not in cheats:
                cheats.add((i, q))

print(len(cheats))
