# Solution to https://projecteuler.net/problem=113

import math
import utilities

LENGTH = 10

cache = dict()

def count_nonbouncy(base, length, increase, decrease):
	if len(base) > 0 and (len(base), base[-1], increase, decrease) in cache:
		return cache[(len(base), base[-1], increase, decrease)]
	if increase and decrease:
		return 0
	if len(base) == length:
		return 1
	if len(base) == 0:
		total = 0
		digits = range(1, 10)
	else:
		total = 1
		digits = range(0, 10)
	for i in digits:
		if len(base) > 0 and i > int(base[-1]):
			total += count_nonbouncy(base + str(i), length, True, decrease)
		elif len(base) > 0 and i < int(base[-1]):
			total += count_nonbouncy(base + str(i), length, increase, True)
		else:
			total += count_nonbouncy(base + str(i), length, increase, decrease)
	if len(base) > 0:
		cache[(len(base), base[-1], increase, decrease)] = total
	return total

def main():
	return count_nonbouncy("", 100, False, False)

if __name__ == "__main__":
	utilities.print_runtime(main)