# advent of code 2021 day 10

with open("day10_in.txt") as f:
	lines = [line.strip() for line in f.readlines()]

inc_lines = []
corrupted_symbols = []
for line in lines:
	line_stack = []
	corrupted = False
	corrupted_char = ''
	for char in line:
		corrupted_char = char
		if char in ['(','[','{','<']:
			line_stack.append(char)
			continue
		if char in [')',']','}','>']:
			if len(line_stack) == 0:
				corrupted = True
				break
			opener = line_stack.pop()
			if opener == '(' and char != ')':
				corrupted = True
				break
			if opener == '[' and char != ']':
				corrupted = True
				break
			if opener == '{' and char != '}':
				corrupted = True
				break
			if opener == '<' and char != '>':
				corrupted = True
				break
	if corrupted == True:
		corrupted_symbols.append(corrupted_char)
	else:
		inc_lines.append(line)

symbol_map = {
	')': 3,
	']': 57,
	'}': 1197,
	'>': 25137
}

total = 0
for sym in corrupted_symbols:
	total += symbol_map[sym]

print(f"Part 1 ans: {total}")

completion_sequences = []
for line in inc_lines:
	line_stack = []
	for char in line:
		corrupted_char = char
		if char in ['(','[','{','<']:
			line_stack.append(char)
		else:
			line_stack.pop()
	line_stack.reverse()
	completion_sequences.append(line_stack)


symbol_map = {
	'(': 1,
	'[': 2,
	'{': 3,
	'<': 4
}

totals = []
for seq in completion_sequences:
	total = 0
	for char in seq:
		total *= 5
		total += symbol_map[char]
	totals.append(total)

totals = sorted(totals)
print(f"Part 2 ans: {totals[int(len(totals)/2)]}")
