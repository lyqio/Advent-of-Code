fl = open("input.txt", "r")
s = fl.read()
fl.close()

d = {}
for line in s.split('\n'):
	c = line.split('-')
	to, fr = c[0], c[1]

	if to in d:
		d[to].append(fr)
		if fr in d:
			d[fr].append(to)
		else:
			d[fr] = [to]
	else:
		d[to] = [fr]
		if fr in d:
			d[fr].append(to)
		else:
			d[fr] = [to]

trips = set()
for vert, adj in d.items():
	for i in range(len(adj)):
		for q in range(i+1, len(adj)):
			# print(vert, adj[i], adj[q])
			if vert.startswith('t') or adj[i].startswith('t') or adj[q].startswith('t'):
				if adj[i] in d[adj[q]] and vert in d[adj[q]] and adj[q] in d[adj[i]] and (adj[i] != adj[q] and adj[i] != vert):
					trips.add(tuple(sorted([adj[i], adj[q], vert])))

print(len(trips))