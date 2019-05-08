# Solution to https://projecteuler.net/problem=105

import itertools
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

def main():
	list = []
	with open("euler-105-data.txt") as f:
		for line in f.readlines():
			dataline = []
			for num in line.split(","):
				dataline.append(int(num))
			list.append(dataline)
	total = 0
	for nums in list:
		if verify_set(nums):
			total += sum(nums)
	return total

if __name__ == "__main__":
	utilities.print_runtime(main)