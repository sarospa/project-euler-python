# Solution to https://projecteuler.net/problem=85

import itertools
import utilities

TARGET = 2000000

def main():
	nearest_count = 0
	nearest_area = 0
	for x in itertools.count(1):
		if utilities.triangle(x) > TARGET:
			break
		for y in itertools.count(1):
			count = utilities.triangle(x) * utilities.triangle(y)
			if abs(TARGET - count) < abs(TARGET - nearest_count):
				nearest_count = count
				nearest_area = x * y
			if count > TARGET:
				break
	return nearest_area

if __name__ == "__main__":
	utilities.print_runtime(main)