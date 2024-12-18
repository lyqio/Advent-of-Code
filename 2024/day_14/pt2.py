import re

fl = open("input.txt", "r")
data = fl.read()
fl.close()

WIDTH =  101
HEIGHT = 103

seen = set()
end = 0
for i in range(1, 10000):
	for line in data.split('\n'):
		a = re.findall("-?\d+", line)
		p = [int(a[0]), int(a[1])]
		v = [int(a[2]), int(a[3])]

		p[0] = (p[0]+ i*v[0])%WIDTH
		p[1] = (p[1]+ i*v[1])%HEIGHT

		seen.add((p[0], p[1]))

	if len(seen) == 500:
		end = i
		break
	seen.clear()

print(end)