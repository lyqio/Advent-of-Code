data = open("in").read()

parts = data.split("\n\n")
init = parts[0].split('\n')
program = parts[1]

reg_a = int(init[0].split(": ")[1])
reg_b = int(init[1].split(": ")[1])
reg_c = int(init[2].split(": ")[1])
instrs = program.split(": ")[1].split(",")
nts = [int(x) for x in instrs]

def get_output(reg_a, reg_b, reg_c, instrs):
	i = 1
	output = []
	while i < len(instrs):
		opcode = instrs[i-1]
		combo = int(instrs[i]) if int(instrs[i]) < 4 else reg_a if instrs[i] == '4' else reg_b if instrs[i] == '5' else reg_c
		literal = int(instrs[i])

		if opcode == '0':
			reg_a = int(reg_a//(2**combo))
		elif opcode == '1':
			reg_b = int(reg_b^literal)
		elif opcode == '2':
			reg_b = combo%8
		elif opcode == '3':
			if reg_a != 0:
				i = literal+1
				continue
		elif opcode == '4':
			reg_b = reg_b^reg_c
		elif opcode == '5':
			output.append(combo % 8)
		elif opcode == '6':
			reg_b = int(reg_a//(2**combo))
		elif opcode == '7':
			reg_c = int(reg_a//(2**combo))

		i += 2
	return output


runnings = [nts[-1]]
for i in range(len(nts)-1, -1, -1):
	new_runnings = []
	for run in runnings:
		for q in range(8):
			if get_output(run+q, reg_b, reg_c, instrs) == nts[i:]:
				new_runnings.append(run+q)

	runnings = [x << 3 for x in new_runnings]

small = float("inf")
for r in runnings:
	if get_output(r//8, reg_b, reg_c, instrs) == nts:
		small = min(small, r//8)

print(small)