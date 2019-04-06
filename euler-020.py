# Solution to https://projecteuler.net/problem=20

import utilities
import math

def main():
	print(sum([int(ch) for ch in str(math.factorial(100))]))

utilities.print_runtime(main)