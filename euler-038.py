# Solution to https://projecteuler.net/problem=38

import utilities

def main():
	largest = 0
	for i in range(2, 100000):
		digits = ""
		n = 1
		while len(digits) < 9:
			digits += str(n * i)
			n += 1
		if ''.join(sorted(digits)) == "123456789" and int(digits) > largest:
			largest = int(digits)
	return largest

if __name__ == "__main__":
	utilities.print_runtime(main)