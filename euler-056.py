# Solution to https://projecteuler.net/problem=56

import utilities

def main():
	return max([sum([int(digit) for digit in str(a**b)]) for a in range(1, 101) for b in range(1, 101)])

if __name__ == "__main__":
	utilities.print_runtime(main)