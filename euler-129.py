# Solution to https://projecteuler.net/problem=129

import itertools
import utilities

TARGET = 1000000

def main():
	best = 0
	for i in itertools.count(TARGET, 10):
		for n in [i + 1, i + 3, i + 7, i + 9]:
			remainder = 1
			count = 1
			while remainder != 0:
				remainder = (remainder * 10 + 1) % n
				count += 1
			if count > TARGET:
				return n

if __name__ == "__main__":
	utilities.print_runtime(main)