# advent of code 2021 day 8
import numpy as np
import time

with open("day8_in.txt") as f:
	lines = [line.strip() for line in f.readlines()]

new_lines = []
for line in lines:
	new_lines.append(line.split())
lines = new_lines

ans = 0
for line in lines:
	for i in range(11, 15):
		if len(line[i]) in [2,4,3,7]:
			ans += 1

print(f"Part 1 ans: {ans}")

new_lines = []
for line in lines:
	new_line = []
	for item in line:
		new_item = []
		for char in item:
			new_item.append(char)
		new_line.append(sorted(new_item))
	new_lines.append(new_line)
lines = new_lines

grand_sum = 0
for line in lines:
	digit_map = {}

	# find 1, 7, 4, 8
	for item in line[:10]:
		if len(item) == 2:
			digit_map[1] = item
		elif len(item) == 3:
			digit_map[7] = item
		elif len(item) == 4:
			digit_map[4] = item
		elif len(item) == 7:
			digit_map[8] = item

	for item in line[:10]:
		# find 3,5,2
		if len(item) == 5:
			intersect_with_1 = list(set(item).intersection(set(digit_map[1])))
			intersect_with_4 = list(set(item).intersection(set(digit_map[4])))
			if len(intersect_with_1) == 2:
				digit_map[3] = item
			elif len(intersect_with_4) == 3:
				digit_map[5] = item
			else:
				digit_map[2] = item

	for item in line[:10]:
		# find 6,9
		if len(item) == 6:
			intersect_with_1 = list(set(item).intersection(set(digit_map[1])))
			intersect_with_5 = list(set(item).intersection(set(digit_map[5])))
			if len(intersect_with_1) == 1:
				digit_map[6] = item
			elif len(intersect_with_5) == 5:
				digit_map[9] = item
			else:
				digit_map[0] = item

	# compute output nums
	output_num = ""
	for item in line[11:]:
		for i in range(10):
			if item == digit_map[i]:
				output_num += str(i)
	grand_sum += int(output_num)

print(f"Part 1 ans: {grand_sum}")



# 2 segments means 1
# 3 segments means 7
# 4 segments means 4
# 7 segments means 8

# 5 segments means 5,2,3
# -- 3 will share 2 segments with 1
# -- 5 will share 3 segments with 4
# -- 2 is the other one
# 6 segments means 0,6,9
# -- 6 will share only 1 segment with 1
# -- 9 shares 5 segments with 5
# -- 0 is the other one