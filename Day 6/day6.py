# advent of code 2021 day 6

with open("day6_in.txt") as f:
	lines = [line.strip() for line in f.readlines()]

numbers = [int(x) for x in lines[0].split(',')]

# create dictionary representation
fish_dict = {}
for num in range(9):
	fish_dict[num] = 0
for num in numbers:
	fish_dict[num] += 1

# each day adjust nums
for i in range(80):
	new_dict = {}
	
	for j in range(8):
		new_dict[j] = fish_dict[j+1]
	new_dict[6] += fish_dict[0]
	new_dict[8] = fish_dict[0]

	fish_dict = new_dict

# sum total
total_fish = 0
for i in range(9):
	total_fish += fish_dict[i]

print(f"Part 1 ans: {total_fish}")

# create dictionary representation
fish_dict = {}
for num in range(9):
	fish_dict[num] = 0
for num in numbers:
	fish_dict[num] += 1

# each day adjust nums
for i in range(256):
	new_dict = {}
	
	for j in range(8):
		new_dict[j] = fish_dict[j+1]
	new_dict[6] += fish_dict[0]
	new_dict[8] = fish_dict[0]

	fish_dict = new_dict

# sum total
total_fish = 0
for i in range(9):
	total_fish += fish_dict[i]


print(f"Part 2 ans: {total_fish}")