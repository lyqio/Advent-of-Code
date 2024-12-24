
fl = open("input.txt", "r")
s = fl.read().split('\n')
fl.close()

def do(num):
	m = ((num*64)^num)%16777216
	c = ((m//32)^m)%16777216
	d = ((c*2048)^c)%16777216
	return d

sm = 0
for i in s:
	v = int(i)
	for q in range(2000):
		v = do(v)
	sm += v

print(sm)