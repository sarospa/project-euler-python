# Solution to https://projecteuler.net/problem=33

import utilities

def main():
	numerator = 1
	denominator = 1
	for i in range(10, 100):
		for j in range(i + 1, 100):
			shared_digit = ''.join(set(str(i)) & set(str(j)))
			other_digits = set(str(i)) ^ set(str(j))
			if len(shared_digit) == 1 and len(other_digits) == 2:
				simple_i = int(str(i).replace(shared_digit, ""))
				simple_j = int(str(j).replace(shared_digit, ""))
				if simple_i != 0 and simple_j != 0 and i / simple_i == j / simple_j and shared_digit != "0":
					numerator *= simple_i
					denominator *= simple_j
	factor = 2
	while factor <= numerator:
		if numerator % factor == 0 and denominator % factor == 0:
			numerator //= factor
			denominator //= factor
		else:
			factor += 1
	return denominator

if __name__ == "__main__":
	utilities.print_runtime(main)