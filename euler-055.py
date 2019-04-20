# Solution to https://projecteuler.net/problem=55

import utilities

def main():
	count = 0
	for i in range(10001):
		n = i
		lychrel = 1
		for i in range(50):
			n = n + int(str(n)[::-1])
			if str(n) == str(n)[::-1]:
				lychrel = 0
				break
		count += lychrel
	return count

if __name__ == "__main__":
	utilities.print_runtime(main)