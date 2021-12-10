# advent of code 2021 day 1

with open("day1_in.txt") as f:
	lines = [line.strip() for line in f.readlines()]

output = 0

for i in range(1, len(lines)):
	if float(lines[i]) > float(lines[i-1]):
		output += 1

print(f"Part 1 ans: {output}")

output = 0
for window_end in range(3, len(lines)):
	this_total = float(lines[window_end]) + float(lines[window_end-1]) + float(lines[window_end-2])
	prev_total = float(lines[window_end-1]) + float(lines[window_end-2]) + float(lines[window_end-3])
	if this_total > prev_total:
		output += 1

print(f"Part 2 ans: {output}")
