# advent of code 2021 day 3

with open("day3_in.txt") as f:
	lines = [line.strip() for line in f.readlines()]

one_counts = []

for i in range(len(lines[0])):
	one_counts.append(0)

for line in lines:
	for i in range(len(line)):
		if line[i] == "1":
			one_counts[i] += 1

gamma_rate = ""
epsilon_rate = ""

for one_count in one_counts:
	if one_count > (len(lines)/2):
		gamma_rate += "1"
		epsilon_rate += "0"
	else:
		gamma_rate += "0"
		epsilon_rate += "1"

def binaryToDecimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal

ans = binaryToDecimal(int(gamma_rate)) * binaryToDecimal(int(epsilon_rate))
print(f"Part 1 answer: {ans}")


oxygen_list = []
oxygen_list.extend(lines)
co2_list = []
co2_list.extend(lines)

def cull_oxy_list_on_bit_idx(bit_idx, oxy_list):
	one_count = 0
	for num in oxy_list:
		if num[bit_idx] == "1":
			one_count += 1
	popular = "1"
	if one_count < len(oxy_list)/2:
		popular = "0"

	to_return = []
	for num in oxy_list:
		if num[bit_idx] == popular:
			to_return.append(num)
	return to_return

def cull_co2_list_on_bit_idx(bit_idx, co2_list):
	one_count = 0
	for num in co2_list:
		if num[bit_idx] == "1":
			one_count += 1
	popular = "1"
	if one_count < len(co2_list)/2:
		popular = "0"

	to_return = []
	for num in co2_list:
		if num[bit_idx] != popular:
			to_return.append(num)
	return to_return

bit_idx = 0
while len(oxygen_list) > 1:
	oxygen_list = cull_oxy_list_on_bit_idx(bit_idx, oxygen_list)
	bit_idx += 1
bit_idx = 0
while len(co2_list) > 1:
	co2_list = cull_co2_list_on_bit_idx(bit_idx, co2_list)
	bit_idx += 1

final_oxygen = binaryToDecimal(int(oxygen_list[0]))
final_co2 = binaryToDecimal(int(co2_list[0]))
print(f"Part 2 answer: {final_oxygen * final_co2}")


