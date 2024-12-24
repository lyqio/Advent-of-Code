import copy, re, itertools

fil = open("input.txt", "r")
data = fil.read()
fil.close() 	

segm = data.split("\n\n")
towels = segm[0].split(', ')
lines = segm[1].split('\n')

cache = {}
def solve(pattern):
	if pattern not in cache:
		if len(pattern) == 0:
			return 1

		subs = ""
		i = 0
		cnt = 0
		for c in pattern:
			i += 1
			subs += c
			if subs in towels:
				cnt += solve(copy.copy(pattern[i:]))

		cache[pattern] = cnt
		return cnt
	else:
		return cache[pattern]

cnt = 0
for line in lines:
	cnt += int(solve(line))
print(cnt)
