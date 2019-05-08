# Solution to https://projecteuler.net/problem=106

import itertools
import utilities

LENGTH = 12

def main():
	total = 0
	for i in range(2, LENGTH):
		subsets = [set(subset) for subset in itertools.combinations(range(1, LENGTH + 1), i)]
		for subset_1 in subsets:
			disjoint_subsets = [set(subset) for subset in itertools.combinations(set(range(1, LENGTH + 1)) - subset_1, i) if sorted(subset) > sorted(subset_1)]
			for subset_2 in disjoint_subsets:
				sorted_sub_1 = sorted(subset_1)
				sorted_sub_2 = sorted(subset_2)
				required_pair = False
				for j in range(len(sorted_sub_1)):
					if sorted_sub_2[j] < sorted_sub_1[j]:
						required_pair = True
						break
				if required_pair:
					total += 1
	return total

if __name__ == "__main__":
	utilities.print_runtime(main)