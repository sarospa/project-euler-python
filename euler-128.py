# Solution to https://projecteuler.net/problem=128

import itertools
import utilities

TARGET = 2000

def main():
	utilities.generate_primes_sieve(1000000)
	prime_set = set(utilities.primes)
	total = 2
	for i in itertools.count(2):
		base = utilities.triangle(i-1) * 6 + 1
		for j in range(7):
			n = base + 1 + j * i
			if j == 6:
				n -= 1
			if j < 6 and j > 0:
				prev_layer = n - (i * j + (i - 1) * (6 - j))
				next_layer = n + (i * (6 - j) + (i + 1) * j)
				candidates = [prev_layer, next_layer - 1, next_layer, next_layer + 1]
			elif j == 0:
				next_layer = n + i * 6
				next_next_layer = n + (i * 2 + 1) * 6
				candidates = [next_layer - 1, next_layer + 1, next_next_layer - 1]
			else: # j == 6
				prev_prev_layer = n - (i * 2 - 1) * 6
				prev_layer = n - i * 6
				next_layer = n + (i + 1) * 6
				candidates = [prev_prev_layer + 1, prev_layer + 1, next_layer - 1]
			count = 0
			for candidate in candidates:
				if abs(n - candidate) in prime_set:
					count += 1
			if count == 3:
				total += 1
				if total == TARGET:
					return n

if __name__ == "__main__":
	utilities.print_runtime(main)