# Solution to https://projecteuler.net/problem=12

import utilities
import math

def main():
	i = 1
	n = 0
	divisor_count = 0
	while divisor_count <= 500:
		divisors = set()
		n = utilities.triangle(i)
		for j in range(1, round(math.sqrt(n) + 1)):
			if n % j == 0:
				divisors.add(j)
				divisors.add(n // j)
		divisor_count = len(divisors)
		i = i + 1
	return n

if __name__ == "__main__":
	utilities.print_runtime(main)