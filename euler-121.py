# Solution to https://projecteuler.net/problem=121

import itertools
import math
import utilities

TURNS = 15

def main():
	numerator = sum([utilities.product(nums) for nums in utilities.powerset(range(1, TURNS + 1)) if len(nums) < (TURNS+1) // 2])
	denominator = math.factorial(TURNS + 1)
	return int(1 / (numerator/denominator))

if __name__ == "__main__":
	utilities.print_runtime(main)