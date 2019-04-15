# Solution to https://projecteuler.net/problem=20

import utilities
import math

def main():
	return sum([int(ch) for ch in str(math.factorial(100))])

if __name__ == "__main__":
	utilities.print_runtime(main)