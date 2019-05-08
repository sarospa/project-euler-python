# Solution to https://projecteuler.net/problem=104

import utilities

DIGITS = "123456789"

def main():
	f1_large = 1
	f2_large = 1
	f1_small = 1
	f2_small = 1
	count = 2
	while True:
		str_fib = str(f2_large) + str(f2_small)
		if len(str_fib) >= 9 and ''.join(sorted(str_fib[-9:])) == DIGITS and ''.join(sorted(str_fib[:9])) == DIGITS:
			return count
		f2_large = f1_large + f2_large
		f1_large = f2_large - f1_large
		if f2_large > 10**20:
			f1_large //= 10
			f2_large //= 10
		f2_small = (f1_small + f2_small) % 10**10
		f1_small = (f2_small - f1_small) % 10**10
		count += 1

if __name__ == "__main__":
	utilities.print_runtime(main)