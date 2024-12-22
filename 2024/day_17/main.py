data = open("in").read()

parts = data.split("\n\n")
init = parts[0].split('\n')
program = parts[1]

reg_a = int(init[0].split(": ")[1])
reg_b = int(init[1].split(": ")[1])
reg_c = int(init[2].split(": ")[1])
instrs = program.split(": ")[1].split(",")

i = 1
while i < len(instrs):
	opcode = instrs[i-1]
	combo = int(instrs[i]) if int(instrs[i]) < 4 else reg_a if instrs[i] == '4' else reg_b if instrs[i] == '5' else reg_c
	literal = int(instrs[i])

	# print(f":: {opcode}({literal})")
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
		print("{},".format(combo % 8), end="")
	elif opcode == '6':
		reg_b = int(reg_a//(2**combo))
	elif opcode == '7':
		reg_c = int(reg_a//(2**combo))

	i += 2
