# Solution to https://projecteuler.net/problem=149

import utilities as utils

SIZE = 2000

def main():
	utils.lagged_fibonacci(SIZE**2)
	largest = 0
	for i in range(1, SIZE**2, SIZE):
		current = 0
		for j in range(i, i + SIZE):
			current += utils.lagged_fib_cache[j]
			if current > largest:
				largest = current
			if current < 0:
				current = 0
	for i in range(1, SIZE + 1):
		current = 0
		for j in range(i, SIZE**2 + 1, SIZE):
			current += utils.lagged_fib_cache[j]
			if current > largest:
				largest = current
			if current < 0:
				current = 0
		current = 0
		for j in range(i, SIZE**2 + 1, SIZE + 1):
			current += utils.lagged_fib_cache[j]
			if current > largest:
				largest = current
			if current < 0:
				current = 0
			if j % SIZE == 0:
				break
		current = 0
		for j in range(i, SIZE**2 + 1, SIZE - 1):
			if j % SIZE == 0:
				break
			current += utils.lagged_fib_cache[j]
			if current > largest:
				largest = current
			if current < 0:
				current = 0
	return largest

if __name__ == "__main__":
	utils.print_runtime(main)