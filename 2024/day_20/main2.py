from heapq import heappush, heappop
import copy, sys
import time
sys.setrecursionlimit(10000)


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

def adjs(pos):
    i, q = pos
    if i-1 > -1 and (i-1, q) not in mp:
        yield 1, (i-1, q)
    if i+1 < len(s) and (i+1, q) not in mp:
        yield 1, (i+1, q)
    if q-1 > -1 and (i, q-1) not in mp:
        yield 1, (i, q-1)
    if q+1 < len(s) and (i, q+1) not in mp:
        yield 1, (i, q+1)

def cheat_adjs(pos):
    i, q = pos
    if i-1 > -1 and (i-1, q):
        yield 1, (i-1, q)
    if i+1 < len(s) and (i+1, q):
        yield 1, (i+1, q)
    if q-1 > -1 and (i, q-1):
        yield 1, (i, q-1)
    if q+1 < len(s) and (i, q+1):
        yield 1, (i, q+1)

pq = []
heappush(pq, (0, start))
dists = {}
for i in range(len(s)):
    for q in range(len(s)):
        dists[(i, q)] = float("inf")

base = None
dists[start] = 0
while len(pq) > 0:
    dist, pos = heappop(pq)
    if pos == (end[0], end[1]):
        base = dist
        break
    for d, adj in adjs(pos):
        if dist + d < dists[adj]:
            dists[adj] = dist+d
            heappush(pq, (dists[adj], adj))

saved = set()
DIST = 100
cache = {}
def dfs(i, q, cheat, visited, score):
    if (i, q, cheat, score) in cache:
        return cache[(i, q, cheat, score)]

    global cnt

    a = set()
    visited.add((i, q))
    if (i, q) == end:
        if base-score >= DIST:
            a.add((i, q, cheat, score))
            return a
        return a

    if cheat == 0:
        for sc, adj in adjs((i, q)):
            if adj not in visited:
                a = a | dfs(adj[0], adj[1], 0, copy.copy(visited), score+sc)
    else:
        for sc, adj in adjs((i, q)):
            if cheat < 20:
                if adj not in visited:
                    a = a | dfs(adj[0], adj[1], 0, copy.copy(visited), score+sc)
            else:
                if adj not in visited:
                    a = a | dfs(adj[0], adj[1], cheat, copy.copy(visited), score+sc)

        for sc, adj in cheat_adjs((i, q)):
            if adj not in visited:
                a = a | dfs(adj[0], adj[1], cheat-1, copy.copy(visited), score+sc)

    cache[(i, q, cheat, score)] = a
    return a

print(len(dfs(start[0], start[1], 20, set(), 0)))