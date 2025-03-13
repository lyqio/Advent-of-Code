from heapq import heappop, heappush

s = str()
with open("input.txt", "r") as fl:
	s = fl.read()


parts = s.split("\n\n")
init = parts[0]
instr = parts[1]

d = {}
for line in init.split('\n'):
	c = line.split(": ")
	d[c[0]] = int(c[1])


seconds = instr.split('\n')
da = True
while da:
	da = False
	for line in seconds:
		q = line.split(" -> ")
		into = q[-1]
		p = q[0].split(' ')

		if p[0] not in d or p[2] not in d:
			da = True
			seconds.append(line)
			continue

		if p[1] == "XOR":
			d[into] = d[p[0]]^d[p[2]]
		elif p[1] == "AND":
			d[into] = d[p[0]]&d[p[2]]
		elif p[1] == "OR":
			d[into] = d[p[0]]|d[p[2]]
	seconds = []

pq = []
for key, val in d.items():
	if key[0] == 'z':
		pq.append((key, val))

z = ""
for i in sorted(pq, key=lambda x: x[0]):
	z += str(i[1])

print(int(z[::-1], 2))