# Solution to https://projecteuler.net/problem=97

import utilities

def main():
	return (28433 * 2**7830457 + 1) % 10**10

if __name__ == "__main__":
	utilities.print_runtime(main)