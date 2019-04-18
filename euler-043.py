# Solution to https://projecteuler.net/problem=43

import itertools
import utilities

def main():
	numbers = [num for num in list(itertools.permutations("0123456789", 10)) if int(num[7] + num[8] + num[9]) % 17 == 0]
	numbers = [num for num in numbers if int(num[6] + num[7] + num[8]) % 13 == 0]
	numbers = [num for num in numbers if int(num[5] + num[6] + num[7]) % 11 == 0]
	numbers = [num for num in numbers if int(num[4] + num[5] + num[6]) % 7 == 0]
	numbers = [num for num in numbers if int(num[3] + num[4] + num[5]) % 5 == 0]
	numbers = [num for num in numbers if int(num[2] + num[3] + num[4]) % 3 == 0]
	return sum([int(''.join(num)) for num in numbers if int(num[1] + num[2] + num[3]) % 2 == 0 and num[0] != '0'])

if __name__ == "__main__":
	utilities.print_runtime(main)