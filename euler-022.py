# Solution to https://projecteuler.net/problem=22

import utilities

def main():
	with open("euler-022-data.txt") as f:
		print(sum([sum([ord(ch) - ord("A") + 1 for ch in name]) * (i + 1) for i, name in enumerate(sorted([name[1:-1] for name in f.read().split(",")]))]))

utilities.print_runtime(main)