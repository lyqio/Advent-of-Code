import copy

fil = open("input.txt", "r")
data = fil.read()
fil.close() 	

data = data.replace(".", "..").replace("#", "##").replace("@", "@.").replace("O", "[]")


# data = """####################
# ##[]..[]......[][]##
# ##[]........@..[].##
# ##..........[][][]##
# ##...........[][].##
# ##..##[]..[]......##
# ##...[]...[]..[]..##
# ##.....[]..[].[][]##
# ##........[]......##
# ####################

# v"""

data = data.split("\n\n")
moves = data[1]

value = None
hsh = {}
lines = data[0].split("\n")
for i in range(len(lines)):
	# print(lines[i])
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

def do_move(i, q, direction):
	global hsh

	if hsh[(i, q)] == '#':
		return False

	if hsh[(i, q)] == '.' and hsh[(i, q+1)] == '.':
		return True

	if hsh[(i, q)] == '[' and hsh[(i, q+1)] == ']':
		if hsh[(i+direction[0], q+direction[1])] == '.' and hsh[(i+direction[0], q+1+direction[1])] == '.':
			hsh[(i+direction[0], q+direction[1])], hsh[(i+direction[0], q+1+direction[1])] = '[', ']'
			hsh[(i, q)], hsh[(i, q+1)] = '.', '.'
			return True

		i += direction[0]
		q += direction[1]

		valid = do_move(i, q, direction) or hsh[(i, q)] == '.'
		valid2 = do_move(i, q+1, direction) or hsh[(i, q+1)] == '.'
		# print("do1 : ", valid, valid2)

		hsh[(i, q)], hsh[(i, q+1)] = '[', ']'
		hsh[(i-direction[0], q)], hsh[(i-direction[0], q+1)] = '.', '.'

		return valid and valid2

	elif hsh[(i, q)] == ']' and hsh[(i, q-1)] == '[':
		q -= 1
		if hsh[(i+direction[0], q+direction[1])] == '.' and hsh[(i+direction[0], q+1+direction[1])] == '.':
			hsh[(i+direction[0], q+direction[1])], hsh[(i+direction[0], q+1+direction[1])] = '[', ']'
			hsh[(i, q)], hsh[(i, q+1)] = '.', '.'
			return True

		i += direction[0]
		q += direction[1]

		valid = do_move(i, q, direction) or hsh[(i, q)] == '.'
		valid2 = do_move(i, q+1, direction) or hsh[(i, q+1)] == '.'
		# print("do2 : ", valid, valid2)

		hsh[(i, q)], hsh[(i, q+1)] = '[', ']'
		hsh[(i-direction[0], q)], hsh[(i-direction[0], q+1)] = '.', '.'

		return valid and valid2

	return False

def check_move(i, q, direction):
	global hsh

	if hsh[(i, q)] == '#':
		return False

	if hsh[(i, q)] == '.' and hsh[(i, q+1)] == '.':
		return True

	if hsh[(i, q)] == '[' and hsh[(i, q+1)] == ']':
		if hsh[(i+direction[0], q+direction[1])] == '.' and hsh[(i+direction[0], q+1+direction[1])] == '.':
			return True

		i += direction[0]
		q += direction[1]

		valid = check_move(i, q, direction) or hsh[(i, q)] == '.'
		valid2 = check_move(i, q+1, direction) or hsh[(i, q+1)] == '.'
		# print("check1 : ", valid, valid2)
		return valid and valid2

	elif hsh[(i, q)] == ']' and hsh[(i, q-1)] == '[':
		q -= 1
		if hsh[(i+direction[0], q+direction[1])] == '.' and hsh[(i+direction[0], q+1+direction[1])] == '.':
			return True

		i += direction[0]
		q += direction[1]

		valid = check_move(i, q, direction) or hsh[(i, q)] == '.'
		valid2 = check_move(i, q+1, direction) or hsh[(i, q+1)] == '.'
		# print("check2 : ", valid, valid2)
		return valid and valid2

	return False

for move in moves:

	if move == '\n':
		continue

	nx, ny = x+directions[move][0], y+directions[move][1]
	if hsh[(nx, ny)] == '.':
		x, y = nx, ny
	elif hsh[(nx, ny)] == '#':
		continue
	elif hsh[(nx, ny)] in ['[', ']']:
		if directions[move][0] != 0:
			if hsh[(nx, ny)] == '[' and hsh[(nx, ny+1)] == ']' or hsh[(nx, ny)] == ']' and hsh[(nx, ny-1)] == '[':
				works = check_move(nx, ny, directions[move])
				if works:
					do_move(nx, ny, directions[move])
					x, y = nx, ny
		else:
			works = False
			e = ny+directions[move][1]
			while hsh[(nx, e)] not in [".", "#"]:
				e += directions[move][1]

			works = hsh[(nx, e)] == '.'

			if works:
				end = ny+directions[move][1]
				while hsh[(nx, end)] not in [".", "#"]:
					hsh[(nx, end)] = "]" if hsh[(nx, end)] == "[" else "["
					end += directions[move][1]
	
				assert hsh[(nx, end)] == '.'
				hsh[(nx, end)] = ']' if hsh[(nx, end-1)] == '[' else '['
				hsh[(nx, ny)] = '.'
				x, y = nx, ny

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
out = out.replace("[]", "O.")
# print("final: \n" + out)

out = out.split('\n')
total = 0
for i in range(len(out)-1):
	for q in range(len(out[0])):
		# print(i, q)
		if out[i][q] == 'O':
			total += (100*i)+q

print total