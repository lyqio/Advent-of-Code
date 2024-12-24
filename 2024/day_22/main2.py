import os

fl = open("input.txt", "r")
s = fl.read().split('\n')
fl.close()

def do(num):
	m = ((num*64)^num)%16777216
	c = ((m//32)^m)%16777216
	d = ((c*2048)^c)%16777216
	return d

def get_prices(num):
	pr = [int(str(num)[-1])]
	for i in range(2000):
		num = do(num)
		pr.append(int(str(num)[-1]))
	return pr

def get_diff(pr):
	d = []
	for i in range(1, len(pr)):
		d.append(pr[i]-pr[i-1])
	return d

def make_dict(diffs, prices):
	dc = {}
	for i in range(4, len(diffs)):
		if tuple(diffs[i-4:i]) in dc:
			continue

		dc[tuple(diffs[i-4:i])] = prices[i]
	return dc

dl = []

for line in s:
	v = int(line.strip())
	pr = get_prices(v)
	df = get_diff(pr)
	dl.append(make_dict(df, pr))


large = 0
c = 0
known = set()
for d in dl:
	print(c, "of", len(dl))
	for key, val in d.items():
		rang = key

		if rang in known:
			continue

		cnt = 0
		for dic in dl:
			if rang in dic:
				cnt += dic[rang]

		known.add(rang)
		large = max(large, cnt)
	c += 1

print(large)