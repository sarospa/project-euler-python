# Solution to https://projecteuler.net/problem=34

import utilities
import math

def main():
	return sum([i for i in range(10, 2500000) if sum([math.factorial(int(ch)) for ch in str(i)]) == i])

if __name__ == "__main__":
	utilities.print_runtime(main)