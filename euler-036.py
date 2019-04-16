# Solution to https://projecteuler.net/problem=36

import utilities
import math

def main():
	return sum([i for i in range(1, 1000000) if str(i) == str(i)[::-1] and bin(i)[2:] == bin(i)[:1:-1]])

if __name__ == "__main__":
	utilities.print_runtime(main)