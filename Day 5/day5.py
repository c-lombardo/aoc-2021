# advent of code 2021 day 5
import numpy as np

with open("day5_in.txt") as f:
	lines = [line.strip() for line in f.readlines()]

cord_list = []
largest_x = 0
largest_y = 0
for l in lines:
	line = l.split()
	x1_y1 = line[0].split(",")
	x2_y2 = line[2].split(",")
	tup1 = tuple([int(item) for item in x1_y1])
	tup2 = tuple([int(item) for item in x2_y2])
	if tup1[0] > largest_x or tup2[0] > largest_x:
		largest_x = max(tup1[0], tup2[0])
	if tup1[1] > largest_y or tup2[1] > largest_y:
		largest_y = max(tup1[1], tup2[1])
	cord_list.append((tup1, tup2))

matrix = np.zeros((largest_y+1,largest_x+1))

for pair in cord_list:
	x1_y1 = pair[0]
	x2_y2 = pair[1]

	# vertical line, same x values
	if x1_y1[0] == x2_y2[0]:
		start = min(x1_y1[1], x2_y2[1])
		end = max(x1_y1[1], x2_y2[1])
		for y in range(start,end+1):
			matrix[y,x1_y1[0]] += 1

	# horizontal line, same y values
	elif x1_y1[1] == x2_y2[1]:
		start = min(x1_y1[0], x2_y2[0])
		end = max(x1_y1[0], x2_y2[0])
		for x in range(start,end+1):
			matrix[x1_y1[1],x] += 1

	# diagonal line, delta y = delta x
	# kinda gross but it works
	elif abs(x1_y1[1]-x2_y2[1]) == abs(x1_y1[0]-x2_y2[0]):
		curr_y = x1_y1[1]
		curr_x = x1_y1[0]
		inc_x = False
		inc_y = False
		if x2_y2[0] > curr_x:
			inc_x = True
		if x2_y2[1] > curr_y:
			inc_y = True
		while curr_x != x2_y2[0] and curr_y != x2_y2[1]:
			matrix[curr_y,curr_x] += 1
			if inc_x:
				curr_x += 1
			else:
				curr_x -= 1
			if inc_y:
				curr_y += 1
			else:
				curr_y -= 1
		matrix[curr_y,curr_x] += 1
		if inc_x:
			curr_x += 1
		else:
			curr_x -= 1
		if inc_y:
			curr_y += 1
		else:
			curr_y -= 1

# set all nums less than 2 -> 0
np.place(matrix, matrix<2, [0])
print(f"Part 2 ans: {np.count_nonzero(matrix)}")