# advent of code 2021 day 7
import numpy as np
import time

with open("day7_in.txt") as f:
	lines = [line.strip() for line in f.readlines()]

nparr = np.array([int(x) for x in lines[0].split(',')])

median = np.median(nparr)

# define vectorized function
calc_distance = np.vectorize(lambda x : abs(median - x))

final_ans = np.sum(calc_distance(nparr))
print(f"Part 1: {int(final_ans)}")



def fuel_consumed(fro, to):
	return_total = 0
	for i in range(1, abs(fro-to) + 1):
		return_total += i
	return return_total

def score_value(val, numpy_arr):
	calc_score = np.vectorize(lambda x : fuel_consumed(val, x))
	return np.sum(calc_score(numpy_arr))

# start at the mean (rounded to nearest int)
best_value = int(round(np.mean(nparr)))
best_final_ans = score_value(best_value, nparr)

# check results for mean+1 and mean-1
final_ans_plus = score_value(best_value+1, nparr)
final_ans_minus = score_value(best_value-1, nparr)

# if the mean is better than mean+1 and mean-1, we're done
if best_final_ans <= min(final_ans_minus, final_ans_plus):
	print(f"Part 2: {best_final_ans}")
	exit(0)

# if we're trying higher values sign = 1, else sign = -1
sign = 1
if final_ans_minus < best_final_ans:
	sign = -1
done = False

# loop for as long as the values are getting better
while not done:
	new_value = best_value + sign
	new_final_ans = score_value(new_value, nparr)
	if new_final_ans < best_final_ans:
		best_value = new_value
		best_final_ans = new_final_ans
	else:
		done = True

print(f"Part 2: {best_final_ans}")


