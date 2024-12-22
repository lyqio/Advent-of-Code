import copy, sys, time

data = open("input.txt", "r").read().split('\n')

start = (0, 0)
end = (0, 0)
for i in range(len(data)):
    for q in range(len(data[0])):
        if data[i][q] == 'S':
            start = (i, q)
        if data[i][q] == 'E':
            end = (i, q)

directions = {
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0)
}

td = (0 ,1)

dist = {}
unx = set()
for i in range(len(data)):
    for q in range(len(data[0])):
        if data[i][q] == '#':
            continue

        for d in directions:
            dist[(i, q, d)] = float("inf")
            unx.add((i, q, d))

dist[(start[0], start[1], td)] = 0

l = time.time()
while len(unx) > 0:
    if time.time()-l > 10:
        print(len(unx))
        l = time.time()

    mn = float("inf")
    u = ()
    for i in unx:
        if dist[i] <= mn:
            mn = dist[i]
            u = i
    unx.remove(u)

    td = u[2]
    for d in directions:
        if (u[0]+d[0], u[1]+d[1], d) not in unx or data[u[0]+d[0]][u[1]+d[1]] == '#':
            continue

        v = (u[0]+d[0], u[1]+d[1], d)
        if d == td:
            alt = dist[u] + 1
            if alt < dist[v]:
                dist[v] = alt
        elif (d[0] == td[0] and d[1] == -td[1]) or (d[0] == -td[0] and d[1] == td[1]):
            alt = dist[u] + 2001
            if alt < dist[v]:
                dist[v] = alt
        else:
            alt = dist[u] + 1001
            if alt < dist[v]:
                dist[v] = alt

m = float("inf")
for d in directions:
    m = min(m, dist[(end[0], end[1], d)])
print(m)