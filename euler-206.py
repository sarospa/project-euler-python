# Solution to https://projecteuler.net/problem=206

import itertools
import math
import utilities

def main():
	for i in itertools.count(10**9, 10):
		if str(i**2)[::2] == "1234567890":
			return i

if __name__ == "__main__":
	utilities.print_runtime(main)