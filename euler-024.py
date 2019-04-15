# Solution to https://projecteuler.net/problem=24

import utilities
import itertools

def main():
	return ''.join(list(itertools.permutations("0123456789"))[999999])

if __name__ == "__main__":
	utilities.print_runtime(main)