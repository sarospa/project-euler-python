# Solution to https://projecteuler.net/problem=17

import utilities

first_digits = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
second_digits = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
tens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

def count_letters(n):
	if n < 10:
		return len(first_digits[n])
	elif n < 20:
		return len(tens[n - 10])
	elif n < 100:
		return len(second_digits[n // 10]) + len(first_digits[n % 10])
	elif n < 1000:
		count = len(first_digits[n // 100]) + len("hundred")
		if n % 100 != 0:
			count = count + len("and") + count_letters(n % 100)
		return count
	elif n == 1000:
		return len("onethousand")
	return 0

def main():
	return sum([count_letters(i) for i in range(1, 1001)])

if __name__ == "__main__":
	utilities.print_runtime(main)