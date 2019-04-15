# Solution to https://projecteuler.net/problem=9

import utilities

def main():
	for a in range(1, 1000):
		for b in range(a, 1000 - a):
			c = 1000 - (a + b)
			if (a ** 2) + (b ** 2) == c ** 2:
				return a * b * c

if __name__ == "__main__":
	utilities.print_runtime(main)