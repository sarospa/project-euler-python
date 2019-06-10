# Solution to https://projecteuler.net/problem=73

import math
import utilities

def main():
	count = 0
	for i in range(4, 120001):
		print(i)
		for j in range(i // 3 + 1, i // 2 + 1):
			if math.gcd(i, j) == 1:
				count += 1
	return count

if __name__ == "__main__":
	utilities.print_runtime(main)