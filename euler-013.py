# Solution to https://projecteuler.net/problem=13

import utilities

def main():
	nums = []
	with open("euler-013-data.txt") as f:
		for line in f.readlines():
			nums.append(int(line))
	print(str(sum(nums))[0:10])

utilities.print_runtime(main)