# Solution to https://projecteuler.net/problem=28

import utilities

def main():
	total = 1
	n = 1
	for i in range(2, 1001, 2):
		total += n * 4 + i * 10
		n += i * 4
	return total

if __name__ == "__main__":
	utilities.print_runtime(main)