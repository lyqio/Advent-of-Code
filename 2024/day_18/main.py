import copy
from heapq import heappush, heappop

fl = open("input.txt", "r")
data = fl.read()
fl.close()

TIMES = 1024
mp = {}
c = 0
for i in data.split('\n'):
	if c >= TIMES:
		break

	a = i.split(",")
	mp[(int(a[0]), int(a[1]))] = '#'
	c += 1

start = (0, 0)
end = (71, 71)

def adjs(pos):
	i, q = pos
	if i-1 > -1 and (i-1, q) not in mp:
		yield 1, (i-1, q)
	if i+1 < end[0] and (i+1, q) not in mp:
		yield 1, (i+1, q)
	if q-1 > -1 and (i, q-1) not in mp:
		yield 1, (i, q-1)
	if q+1 < end[1] and (i, q+1) not in mp:
		yield 1, (i, q+1)

pq = []
heappush(pq, (0, start))
dists = {}
for i in range(end[0]):
	for q in range(end[1]):
		dists[(i, q)] = float("inf")

dists[start] = 0
while len(pq) > 0:
	dist, pos = heappop(pq)
	if pos == (end[0]-1, end[1]-1):
		print(dist)
		break
	for d, adj in adjs(pos):
		if dist + d < dists[adj]:
			dists[adj] = dist+d
			heappush(pq, (dists[adj], adj))
