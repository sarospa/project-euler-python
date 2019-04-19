# Solution to https://projecteuler.net/problem=52

import utilities

def main():
	power = 5
	while True:
		for i in range(10**power, 10**(power+1) // 6):
			if len({''.join(sorted(str(i * j))) for j in range(1, 7)}) == 1:
				return i

if __name__ == "__main__":
	utilities.print_runtime(main)