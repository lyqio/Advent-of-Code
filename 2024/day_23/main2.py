import copy

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

def find_match(cur, d, adj):
	for i in adj:
		if i in cur:
			continue

		found = None
		for q in cur:
			found = q
			if q not in d[i]:
				found = None
				break

		if found is None:
			continue

		cur.append(i)
		break
	return cur

largest = 0
ans = tuple()
for vert, adj in d.items():
	cur = [vert]
	last = 0
	while last != len(cur):
		last = len(cur)
		cur = find_match(copy.copy(cur), d, adj)

	if len(cur) > largest:
		largest = len(cur)
		ans = tuple(cur)

a = 0
for i in sorted(list(ans)):
	if a == len(ans)-1:
		print(f"{i}", end="")
		break

	print(f"{i},", end="")
	a += 1
print()
