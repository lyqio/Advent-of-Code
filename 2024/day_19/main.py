import copy, re, itertools

fil = open("input.txt", "r")
data = fil.read()
fil.close() 	

segm = data.split("\n\n")
towels = segm[0].split(', ')
lines = segm[1].split('\n')

def solve(towels, pattern):
	if len(pattern) == 0:
		return True

	subs = ""
	i = 0
	for c in pattern:
		i += 1
		subs += c
		if subs in towels:
			if solve(towels, copy.copy(pattern[i:])):
				return True

	return False

# print(solve("r, wr, b, g, bwu, rb, gb, br".split(", "), "brwrr"))

cnt = 0
for line in lines:
	cnt += int(solve(towels, line))
print(cnt)
