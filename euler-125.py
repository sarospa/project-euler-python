# Solution to https://projecteuler.net/problem=125

import utilities

MAX = 10**8

def main():
	start = 1
	end = 2
	sum_val = start**2 + end**2
	palindromes = set()
	while True:
		if str(sum_val) == str(sum_val)[::-1]:
			palindromes.add(sum_val)
		end += 1
		sum_val += end**2
		if sum_val >= MAX:
			end = start + 2
			start = start + 1
			sum_val = start**2 + end**2
			if sum_val >= MAX:
				break
	return sum(palindromes)

if __name__ == "__main__":
	utilities.print_runtime(main)