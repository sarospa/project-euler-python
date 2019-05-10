# Solution to https://projecteuler.net/problem=122

import itertools
import math
import utilities

MAX = 200

def main():
	step_set = set([(1,)])
	results = dict()
	count = 0
	unfound = set(range(2, MAX + 1))
	while len(unfound) > 0:
		count += 1
		new_step_set = set()
		for group in step_set:
			combos = list(itertools.combinations_with_replacement(group, 2))
			for combo in combos:
				sum_val = sum(combo)
				if sum_val not in group and sum_val <= MAX:
					new_step_set.add(tuple(sorted(group + (sum_val,))))
					if sum_val in unfound:
						results[sum_val] = count
						unfound.remove(sum_val)
		for key in list(results.keys()):
			if key + 1 in unfound:
				results[key + 1] = results[key] + 1
				if key + 1 in unfound:
					unfound.remove(key + 1)
		step_set = new_step_set
	return sum(results.values())

if __name__ == "__main__":
	utilities.print_runtime(main)