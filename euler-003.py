# Solution to https://projecteuler.net/problem=3

import utilities

def main():
	term = 600851475143
	p = 2
	while term > p:
		while term % p == 0:
			term = int(term / p)
		p = p + 1
	return term

if __name__ == "__main__":
	utilities.print_runtime(main)