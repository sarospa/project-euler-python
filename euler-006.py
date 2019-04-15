# Solution to https://projecteuler.net/problem=6

import utilities

def main():
	sum_of_squares = sum([i ** 2 for i in range(1, 101)])
	square_of_sums = sum(range(1, 101)) ** 2
	return square_of_sums - sum_of_squares

if __name__ == "__main__":
	utilities.print_runtime(main)