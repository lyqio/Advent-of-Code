from heapq import heappop, heappush
from collections import defaultdict

s = str()
with open("input.txt", "r") as fl:
	s = fl.read()


parts = s.split("\n\n")
init = parts[0]
instr = parts[1]

d = defaultdict(lambda: ("NON", "NON", "NON"))

for i in init.split("\n"):
    c = i.split(": ")
    d[c[0]] = ("NON", "NON", "NON")

for i in instr.split("\n"):
    ps = i.replace(" -> ", " ").split(" ")
    d[ps[3].strip()] = (ps[0], ps[2], ps[1])


weird = []
for key, val in d.items():
    if key[0] == 'z':
        if key != "z45" and val[2] != "XOR":
            weird.append(key)

        if key == "z00" and (val[0] not in ["x00", "y00"] or val[1] not in ["x00", "y00"] or val[0] != val[1]):
            weird.append(key)
        
        if key != "z00" and val[0][0] == 'x' or val[0][0] == 'y' or val[1][0] == 'x' or val[1][0] == 'y':
            weird.append(key)

    if val in d and d[val[0]][2] != "AND" or d[val[1]][2] != "AND":
        weird.append(key)

    if val in d and val != "x00" and val[2] == "AND" and d[val[2]][2] == "AND":
        weird.append(key)

    if val in d and key[0] != 'z' and val[2] == "XOR" and ((d[val[0]][2], d[val[1]][2]) == ("OR", "XOR") or (d[val[0]][2], d[val[1]][2]) == ("XOR", "OR")):
        weird.append(key)

print(sorted(weird))
