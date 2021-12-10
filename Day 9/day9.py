# advent of code 2021 day 9

with open("day9_in.txt") as f:
	lines = [line.strip() for line in f.readlines()]

height_map = []
for line in lines:
	new_line = []
	for num in line:
		new_line.append(int(num))
	height_map.append(new_line)

risk_level_total = 0
for row in range(len(height_map)):
	for col in range(len(height_map[0])):
		value = height_map[row][col]
		if row != 0 and height_map[row-1][col] <= value:
			continue
		if row != len(height_map)-1 and height_map[row+1][col] <= value:
			continue
		if col != 0 and height_map[row][col-1] <= value:
			continue
		if col != len(height_map[0])-1 and height_map[row][col+1] <= value:
			continue
		risk_level_total += value+1

print(f"Part 1 ans: {risk_level_total}")

def get_basin(height_map, row, col, basin_set):
	if height_map[row][col] == 9:
		return []

	basin_set.add((row,col))
	# check up, left, down, right
	if row != 0 and (not (row-1,col) in basin_set):
		basin_set.update(get_basin(height_map, row-1, col, basin_set))
	if col != 0 and (not (row,col-1) in basin_set):
		basin_set.update(get_basin(height_map, row, col-1, basin_set))
	if row != len(height_map)-1 and (not (row+1,col) in basin_set):
		basin_set.update(get_basin(height_map, row+1, col, basin_set))
	if col != len(height_map[0])-1 and (not (row,col+1) in basin_set):
		basin_set.update(get_basin(height_map, row, col+1, basin_set))

	return basin_set

basin_list = []
for row in range(len(height_map)-1):
	for col in range(len(height_map[0])-1):
		# check if the coordinate is already in a basin
		found = False
		for basin in basin_list:
			if (row,col) in basin:
				found = True
				break
		if found or height_map[row][col] == 9:
			continue
		basin = get_basin(height_map, row, col, set())
		basin_list.append(basin)

lengths = []
for basin in basin_list:
	lengths.append(len(basin))
final_ans = 1
for val in sorted(lengths)[-3:]:
	final_ans *= val
print(f"Part 2 ans: {final_ans}")
