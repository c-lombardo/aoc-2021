# advent of code 2021 day 10

with open("day11_in.txt") as f:
	lines = [line.strip() for line in f.readlines()]

new_lines = []
for line in lines:
	new_line = []
	for n in line:
		new_line.append(int(n))
	new_lines.append(new_line)
lines = new_lines
pt2_lines = new_lines

def step(board):
	flash_count = 0

	# set up array to keep track of if each octopus has flashed this turn
	has_flashed = []
	for i in range(10):
		line = [False for j in range(10)]
		has_flashed.append(line)

	# increment each octopus by 1
	new_board = []
	for line in board:
		new_line = []
		for n in line:
			new_line.append(n+1)
		new_board.append(new_line)

	done = False
	while not done:
		done = True
		for row in range(10):
			for col in range(10):
				# if an octopus is +9 and hasn't flashed yet, increase the octs around it
				if new_board[row][col] > 9 and not has_flashed[row][col]:
					done = False
					has_flashed[row][col] = True
					flash_count += 1
					# increase vertically + horizontally adjacent octs
					if row != 0:
						new_board[row-1][col] += 1
					if row != 9:
						new_board[row+1][col] += 1
					if col != 0:
						new_board[row][col-1] += 1
					if col != 9:
						new_board[row][col+1] += 1
					# increast diagonal octs
					if row != 0 and col != 0:
						new_board[row-1][col-1] += 1
					if row != 0 and col != 9:
						new_board[row-1][col+1] += 1
					if row != 9 and col != 0:
						new_board[row+1][col-1] += 1
					if row != 9 and col != 9:
						new_board[row+1][col+1] += 1

	# set all flashed octopi to 0
	for row in range(10):
		for col in range(10):
			if has_flashed[row][col]:
				new_board[row][col] = 0

	return new_board, flash_count

total_flashes = 0
for i in range(196):
	result = step(lines)
	lines = result[0]
	total_flashes += result[1]

print(f"Part 1 ans: {total_flashes}")

done = False
step_num = 0
while True:
	step_num += 1
	result = step(pt2_lines)
	if result[1] == 100:
		break
	pt2_lines = result[0]

print(f"Part 2 ans: {step_num}")