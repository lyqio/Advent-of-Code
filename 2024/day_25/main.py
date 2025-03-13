s = str()
with open("input.txt", "r") as fl:
	s = fl.read()

parts = s.split("\n\n")

locks = []
keys = []
for item in parts:
	if item[0][0] == '.':
		it = item.split('\n')
		l = []
		for i in range(len(it[0])):
			r = -1
			for q in range(len(it)):
				if it[q][i] == '#':
					r += 1
			l.append(r)
		locks.append(l)
	else:
		it = item.split('\n')[::-1]
		l = []
		for i in range(len(it[0].strip())):
			r = -1
			for q in range(len(it)):
				if it[q][i] == '#':
					r += 1
			l.append(r)
		keys.append(l)

cnt = 0
for lock in locks:
	for key in keys:
		works = True
		for i in range(len(lock)):
			if lock[i] + key[i] >= 6:
				works = False
		# if works:
		# 	print(f"lock {lock} and key {key} works")
		# else:
		# 	print(f"lock {lock} and key {key} overlap")
		cnt += int(works)

print(cnt)