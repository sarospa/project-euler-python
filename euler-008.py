# Solution to https://projecteuler.net/problem=8

import utilities

def main():
	with open("euler-008-data.txt") as f:
		large_num = f.read()
	n = 0
	for i in range(0, len(large_num) - 13):
		val = 1
		for j in range(i, i + 13):
			val = val * int(large_num[j])
		if val > n:
			n = val
	return n

if __name__ == "__main__":
	utilities.print_runtime(main)