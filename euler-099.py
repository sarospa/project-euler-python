# Solution to https://projecteuler.net/problem=99

import utilities

def main():
	with open("euler-099-data.txt") as f:
		pairs = [[int(num) for num in line.split(",")] for line in f.read().split()]
	index_1 = 0
	index_2 = 1
	while index_1 < len(pairs) and index_2 < len(pairs):
		min_exp = min(pairs[index_1][1], pairs[index_2][1])
		mod_exp_1 = pairs[index_1][1] / min_exp
		mod_exp_2 = pairs[index_2][1] / min_exp
		mod_result_1 = pairs[index_1][0]**mod_exp_1
		mod_result_2 = pairs[index_2][0]**mod_exp_2
		if mod_result_1 < mod_result_2:
			index_1 = max(index_1, index_2) + 1
		else:
			index_2 = max(index_1, index_2) + 1
	return min(index_1, index_2) + 1

if __name__ == "__main__":
	utilities.print_runtime(main)