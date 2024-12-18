import copy

fil = open("input.txt", "r")
data = fil.read()
fil.close() 	

data = data.split("\n\n")
moves = data[1]

value = None
hsh = {}
lines = data[0].split("\n")
for i in range(len(lines)):
	for q in range(len(lines[i])):
		if lines[i][q] == '@':
			value = (i, q)

		hsh[(i, q)] = lines[i][q]

hsh[value] = '.'
assert value != None
x, y = value[0], value[1]

directions = {
	"^": (-1, 0),
	">": (0, 1),
	"v": (1, 0),
	"<": (0, -1)
}

for move in moves:
	if move == '\n':
		continue

	nx, ny = x+directions[move][0], y+directions[move][1]
	if hsh[(nx, ny)] == '.':
		x, y = nx, ny
	elif hsh[(nx, ny)] == '#':
		continue
	elif hsh[(nx, ny)] == 'O':
		if hsh[(nx+directions[move][0], ny+directions[move][1])] == '.':
			hsh[(nx+directions[move][0], ny+directions[move][1])] = 'O'
			hsh[(nx, ny)] = '.'
			x, y, = nx, ny
		elif hsh[(nx+directions[move][0], ny+directions[move][1])] == 'O':
			fnx, fny = copy.deepcopy(nx), copy.deepcopy(ny)
			while hsh[(nx, ny)] == 'O':
				nx, ny = nx+directions[move][0], ny+directions[move][1]
			
			if hsh[(nx, ny)] == '.':
				hsh[(fnx, fny)] = '.'
				x, y = fnx, fny
				hsh[(nx, ny)] = 'O'

	# print("\nMove: {}\n".format(move))
	# for i in range(len(lines)):
	# 	a = ""
	# 	for q in range(len(lines[i])):
	# 		a += hsh[(i, q)] if (x, y) != (i, q) else "@"
	# 	print(a)

out = ""
for i in range(len(lines)):
	a = ""
	for q in range(len(lines[i])):
		a += hsh[(i, q)] if (x, y) != (i, q) else "@"
	out += a + '\n'

out = out.split('\n')
total = 0
for i in range(len(out)-1):
	for q in range(len(out[0])):
		# print(i, q)
		if out[i][q] == 'O':
			total += (100*i)+q

print total