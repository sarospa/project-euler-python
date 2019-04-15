# Solution to https://projecteuler.net/problem=1

import utilities

def main():
	n = 0
	for i in range(1, 1000):
		if i % 3 == 0 or i % 5 == 0:
			n = n + i
	return n

if __name__ == "__main__":
	utilities.print_runtime(main)