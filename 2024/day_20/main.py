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

    def cheat_adjs(pos):
        i, q = pos
        if i-2 > -1 and (i-2, q) not in mp:
            yield 2, (i-2, q)
        if i+2 < len(data) and (i+2, q) not in mp:
            yield 2, (i+2, q)
        if q-2 > -1 and (i, q-2) not in mp:
            yield 2, (i, q-2)
        if q+2 < len(data) and (i, q+2) not in mp:
            yield 2, (i, q+2)

        if q-1 > -1 and i-1 > -1 and (i-1, q-1) not in mp:
            yield 2, (i-1, q-1)
        if q-1 > -1 and i+1 < len(data) and (i+1, q-1) not in mp:
            yield 2, (i+1, q-1)
        if q+1 < len(data) and i-1 > -1 and (i-1, q+1) not in mp:
            yield 2, (i-1, q+1)
        if q+1 < len(data) and i+1 < len(data) and (i+1, q+1) not in mp:
            yield 2, (i+1, q+1)


    pq = []
    heappush(pq, (0, start))
    dists = {}
    for i in range(len(data)):
        for q in range(len(data)):
            dists[(i, q)] = float("inf")

    base = None
    dists[start] = 0
    while len(pq) > 0:
        dist, pos = heappop(pq)
        if pos == (end[0], end[1]):
            return dist
            break
        for d, adj in adjs(pos):
            if dist + d < dists[adj]:
                dists[adj] = dist+d
                heappush(pq, (dists[adj], adj))

base = go(s)
cnt = 0
DIST = 100
for i in range(len(s)):
    print(i)
    for q in range(len(s[0])):
        if s[i][q] != '#':
            continue

        s[i] = s[i][:q] + '.' + s[i][q+1:]
        del mp[(i, q)]

        if base-go(s) >= DIST:
            cnt += 1
        s[i] = s[i][:q] + '#' + s[i][q+1:]
        mp[(i, q)] = True

print(cnt)
