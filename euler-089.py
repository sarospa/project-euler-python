# Solution to https://projecteuler.net/problem=89

import utilities

numeral_values = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

def roman_to_int(roman):
	total = 0
	prev_value = 0
	value = 0
	for ch in roman:
		value = numeral_values[ch]
		if value > prev_value:
			value -= prev_value
		else:
			total += prev_value
		prev_value = value
	total += prev_value
	return total

def int_to_roman(n):
	roman = ''.join(["M" for i in range(n // 1000)])
	n %= 1000
	if n >= 900:
		roman += "CM"
	elif n >= 500:
		roman += "D" + ''.join(["C" for i in range((n - 500) // 100)])
	elif n >= 400:
		roman += "CD"
	else:
		roman += ''.join(["C" for i in range(n // 100)])
	n %= 100
	if n >= 90:
		roman += "XC"
	elif n >= 50:
		roman += "L" + ''.join(["X" for i in range((n - 50) // 10)])
	elif n >= 40:
		roman += "XL"
	else:
		roman += ''.join(["X" for i in range(n // 10)])
	n %= 10
	if n >= 9:
		roman += "IX"
	elif n >= 5:
		roman += "V" + ''.join(["I" for i in range(n - 5)])
	elif n >= 4:
		roman += "IV"
	else:
		roman += ''.join(["I" for i in range(n)])
	return roman

def main():
	numerals_list = []
	with open("euler-089-data.txt") as f:
		numerals_list = f.read().split()
	start_char_count = sum([len(numerals) for numerals in numerals_list])
	numerals_list = [int_to_roman(roman_to_int(numerals)) for numerals in numerals_list]
	end_char_count = sum([len(numerals) for numerals in numerals_list])
	return start_char_count - end_char_count

if __name__ == "__main__":
	utilities.print_runtime(main)