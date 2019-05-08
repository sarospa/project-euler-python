# Solution to https://projecteuler.net/problem=103

import itertools
import math
import utilities

def verify_set(nums):
	if nums is None:
		return False
	last_max = 0
	for i in range(1, len(nums)):
		combos = list(itertools.combinations(nums, i))
		sums = {sum(combo) for combo in combos}
		if len(combos) != len(sums) or min(sums) <= last_max:
			return False
		last_max = max(sums)
	return True

def generate_minimal_set(cur_set, target_length, best_sum):
	if len(cur_set) == target_length:
		return cur_set
	if sum(cur_set) >= best_sum:
		return None
	best_set = None
	for i in itertools.count(max(cur_set, default=0) + 1):
		sorted_set = sorted(cur_set)
		if (len(sorted_set) >= 2 and i >= sorted_set[0] + sorted_set[1]) or sum(cur_set) + sum(range(i, i + (target_length - len(cur_set)))) >= best_sum:
			return best_set
		gen_set = cur_set.copy()
		gen_set.add(i)
		if verify_set(gen_set):
			new_set = generate_minimal_set(gen_set, target_length, best_sum)
			if new_set is not None and sum(new_set) < best_sum:
				best_set = new_set
				best_sum = sum(new_set)

def main():
	return ''.join([str(num) for num in sorted(generate_minimal_set(set(), 7, 300))])

if __name__ == "__main__":
	utilities.print_runtime(main)