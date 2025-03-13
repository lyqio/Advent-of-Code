import itertools
from heapq import heappush, heappop

dists = {}
prev = {}
def dijkstra(data, start, end):
    global dists
    global prev

    mp = {}
    for i in range(len(data)):
        for q in range(len(data[0])):
            if data[i][q] == '#':
                mp[(i, q)] = True

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
            return dist
        for d, adj in adjs(pos):
            if dist + d < dists[adj]:
                dists[adj] = dist+d
                prev[adj] = pos
                heappush(pq, (dists[adj], adj))

    return None


def trace_path(prev, start, end):
    path = []
    path.append(end)
    while end != start:
        end = prev[end]
        if end == None:
            return
        path.append(end)
    return path 


s = str()
with open("input.txt", "r") as fl:
	s = fl.read().strip()

grid = """#####
#789#
#456#
#123#
##0A#
#####"""

grid2 = """#####
##^A#
#<v>#
#####"""

def find(g, a):
    for i in range(len(g)):
        for q in range(len(g[0])):
            if g[i][q] == a:
                return (i, q)
    return (-1, -1)

def search(g, target):
    global prev
    global dist

    pos = find(g, 'A')
    path = []
    for item in target:
        end = find(g, item)
        dijkstra(g, pos, end)
        p = list(trace_path(prev, pos, end))[::-1]

        l = None
        for point in p:
            if l == None:
                l = point
                continue

            diff = (point[0]-l[0], point[1]-l[1])
            if diff == (0, 1):
                path.append('>')
            elif diff == (1, 0):
                path.append('v')
            elif diff == (0, -1):
                path.append('<')
            elif diff == (-1, 0):
                path.append('^')
            
            l = point
        path.append('A')
        pos = end
        prev = {}
        dist = {}

    return path

def optimise(s):
    for i in range(2, len(s)):
        if s[i] == s[i-2] and s[i-1] != s[i] and s[i] != 'A' and s[i-1] != 'A':
            ls = list(s)
            ls[i], ls[i-1] = ls[i-1], ls[i]
            s = "".join(ls)
    return s

for line in s.split("\n"):
    once = optimise("".join(search(grid.split("\n"), line)))
    twice = optimise("".join(search(grid2.split("\n"), once)))
    thrice = ("".join(search(grid2.split("\n"), twice)))
    print(thrice)
    print(twice)
    print(once)
    print(len(thrice))
