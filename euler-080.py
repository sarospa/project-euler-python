# Solution to https://projecteuler.net/problem=80

import math
import utilities

def main():
	total = 0
	for n in range(2, 100):
		sum = 0
		term = int(math.sqrt(n))
		if term**2 == n:
			continue
		target = n
		for i in range(100):
			sum += term % 10
			target *= 100
			term *= 10
			while term**2 < target:
				term += 1
			term -= 1
		total += sum
	return total

if __name__ == "__main__":
	utilities.print_runtime(main)