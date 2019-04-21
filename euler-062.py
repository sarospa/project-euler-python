# Solution to https://projecteuler.net/problem=62

import itertools
import utilities

def main():
	digits = 1
	start_value = 1
	cubes_group = list([sorted(str(n)) for n in itertools.takewhile(lambda n: len(str(n)) <= digits, map(lambda n: n**3, itertools.count(1))) if len(str(n)) == digits])
	for i in itertools.count(1):
		count = 0
		cube = i ** 3
		cube_digits = sorted(str(cube))
		if len(cube_digits) > digits:
			start_value = i
			digits = len(cube_digits)
			cubes_group = list([sorted(str(n)) for n in itertools.takewhile(lambda n: len(str(n)) <= digits, map(lambda n: n**3, itertools.count(1))) if len(str(n)) == digits])
		for cube2_digits in cubes_group:
			if cube_digits == cube2_digits:
				count += 1
			elif len(cube_digits) < len(cube2_digits):
				break
		if count == 5:
			return cube

if __name__ == "__main__":
	utilities.print_runtime(main)