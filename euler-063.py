# Solution to https://projecteuler.net/problem=63

import itertools
import utilities

def main():
	count = 0
	for a in range(1, 10):
		for b in itertools.count(1):
			digits = len(str(a**b))
			if digits == b:
				count += 1
			elif digits < b:
				break
	return count

if __name__ == "__main__":
	utilities.print_runtime(main)