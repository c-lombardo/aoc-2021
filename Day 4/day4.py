# advent of code 2021 day 4

with open("day4_in.txt") as f:
	lines = [line.strip() for line in f.readlines()]

drawn_nums = lines[0].split(",")
num_boards = (len(lines) - 1) / 6

boards = []
for i in range(2, len(lines)-1, 6):
	board = []
	for j in range(i, i+5):
		row = lines[j].split()
		board.append(row)
	boards.append(board)

pt2_boards = []
for board in boards:
	pt2_board = []
	for row in board:
		pt2_board.append(row.copy())
	pt2_boards.append(pt2_board)
pt2_drawn_nums = drawn_nums.copy()

def is_win(board):
	for row in board:
		win = True
		for num in row:
			if num != "X":
				win = False
		if win:
			return True

	for col in range(5):
		win = True
		for row in range(5):
			if board[row][col] != "X":
				win = False
		if win:
			return True

	return False


winning_board = []
draw_num = -1
while True:
	draw_num = drawn_nums.pop(0)
	for i in range(len(boards)):
		for j in range(len(boards[i])):
			for k in range(len(boards[i][j])):
				if boards[i][j][k] == draw_num:
					boards[i][j][k] = "X"
	win = False
	for board in boards:
		if is_win(board):
			winning_board = board
			win = True
			break
	if win:
		break

unmarked_sum = 0
for row in winning_board:
	for num in row:
		if num != "X":
			unmarked_sum += int(num)

print(f"Part 1 ans: {unmarked_sum*int(draw_num)}")

losing_board = []
draw_num = -1
while True:
	draw_num = pt2_drawn_nums.pop(0)
	for i in range(len(pt2_boards)):
		for j in range(len(pt2_boards[i])):
			for k in range(len(pt2_boards[i][j])):
				if pt2_boards[i][j][k] == draw_num:
					pt2_boards[i][j][k] = "X"
	over = False
	for board in pt2_boards:
		if is_win(board):
			pt2_boards.remove(board)
			if len(pt2_boards) == 0:
				over = True
				losing_board = board
	if over:
		break

unmarked_sum = 0
for row in losing_board:
	for num in row:
		if num != "X":
			unmarked_sum += int(num)

print(f"Part 2 ans: {unmarked_sum*int(draw_num)}")