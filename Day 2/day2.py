# advent of code 2021 day 2

with open("day2_in.txt") as f:
	lines = [line.strip() for line in f.readlines()]

depth = 0
horiz = 0

for line in lines:
	line_list = line.split()
	if line_list[0] == "forward":
		horiz += int(line_list[1])
	elif line_list[0] == "down":
		depth += int(line_list[1])
	elif line_list[0] == "up":
		depth -= int(line_list[1])

print(f"Part 1 answer: {horiz*depth}")

depth = 0
horiz = 0
aim = 0

for line in lines:
	line_list = line.split()
	if line_list[0] == "forward":
		horiz += int(line_list[1])
		depth += (int(aim) * int(line_list[1]))
	elif line_list[0] == "down":
		aim += int(line_list[1])
	elif line_list[0] == "up":
		aim -= int(line_list[1])

print(f"Part 2 answer: {horiz*depth}")