# Solution to https://projecteuler.net/problem=19

import utilities

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def main():
	day = 1
	month = 0
	year = 1901
	count = 0
	while year < 2001:
		days_in_month = months[month]
		if month == 1 and ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
			days_in_month += 1
		day = (day + months[month]) % 7
		if day == 6:
			count += 1
		month += 1
		if month >= 12:
			month = 0
			year += 1
	return count

if __name__ == "__main__":
	utilities.print_runtime(main)