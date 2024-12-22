import copy, itertools

fil = open("input.txt", "r")
data = fil.read()
fil.close() 	

segm = data.split("\n\n")
towels = segm[0].split(', ')
lines = segm[1].split('\n')

for line in lines:
	for twls in list(itertools.permutations(towels)):
		for towel in twls:
