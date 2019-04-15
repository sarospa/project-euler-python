# Solution to https://projecteuler.net/problem=13

import utilities

def main():
	nums = []
	with open("euler-013-data.txt") as f:
		for line in f.readlines():
			nums.append(int(line))
	return str(sum(nums))[0:10]

if __name__ == "__main__":
	utilities.print_runtime(main)