# Solution to https://projecteuler.net/problem=26

import utilities
import math

def main():
	longest_cycle = 0
	value = 0
	for i in range(2, 1000):
		power_of_ten = 10**(int(math.log10(i))+1)
		remainders = []
		remainder = power_of_ten % i
		while remainder not in remainders and remainder != 0:
			power_of_ten *= 10
			remainders.append(remainder)
			remainder = power_of_ten % i
		if remainder == 0:
			cycle = 0
		else:
			cycle = len(remainders) - remainders.index(remainder)
		if cycle > longest_cycle:
			longest_cycle = cycle
			value = i
	return value

if __name__ == "__main__":
	utilities.print_runtime(main)