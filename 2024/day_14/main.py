import re

fl = open("input.txt", "r")
data = fl.read()
fl.close()

WIDTH =  101
HEIGHT = 103

grid = [0, 0, 0, 0]
positions = []
for line in data.split('\n'):
	a = re.findall("-?\d+", line)
	p = [int(a[0]), int(a[1])]
	v = [int(a[2]), int(a[3])]

	for i in range(100):
		new_p1 = (p[0]+v[0])
		new_p2 = (p[1]+v[1])
		if new_p1 < 0:
			p[0] = WIDTH+new_p1
		else:
			p[0] = new_p1%WIDTH
		if new_p2 < 0:
			p[1] = HEIGHT+new_p2
		else:
			p[1] = new_p2%HEIGHT


	if p[0] < WIDTH // 2 and p[1] < HEIGHT // 2:
		grid[0] += 1
	if p[0] < WIDTH // 2 and p[1] >= (HEIGHT // 2)+1:
		grid[1] += 1
	if p[0] >= (WIDTH // 2)+1 and p[1] < HEIGHT // 2:
		grid[2] += 1
	if p[0] >= (WIDTH // 2)+1 and p[1] >= (HEIGHT//2)+1:
		grid[3] += 1

total = 1
for i in grid:
	total *= i

print(total)