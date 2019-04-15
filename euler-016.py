# Solution to https://projecteuler.net/problem=16

import utilities

def main():
	return sum([int(ch) for ch in str(2 ** 1000)])

if __name__ == "__main__":
	utilities.print_runtime(main)