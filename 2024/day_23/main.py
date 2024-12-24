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
for node, adjs in d.items():
	for i in range(len(adjs)):
		for q in range(len(adjs)):
			if node.startswith('t') or adjs[i].startswith('t') or adjs[q].startswith('t') and (node != adjs[i] and node != adjs[q] and adjs[i] != adjs[q]):
				trips.add(tuple(sorted((node, adjs[i], adjs[q]))))

print(sorted(trips))
print(len(trips))