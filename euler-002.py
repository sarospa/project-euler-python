# Solution to https://projecteuler.net/problem=2

import utilities

def main():
	f1 = 1
	f2 = 2
	n = 0
	while f2 < 4000000:
		if f2 % 2 == 0:
			n = n + f2
		f2 = f1 + f2
		f1 = f2 - f1
	return n

if __name__ == "__main__":
	utilities.print_runtime(main)