# Solution to https://projecteuler.net/problem=24

import utilities
import itertools

def main():
	print(''.join(list(itertools.permutations("0123456789"))[999999]))

utilities.print_runtime(main)