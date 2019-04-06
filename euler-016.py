# Solution to https://projecteuler.net/problem=16

import utilities

def main():
	print(sum([int(ch) for ch in str(2 ** 1000)]))

utilities.print_runtime(main)