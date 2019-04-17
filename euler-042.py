# Solution to https://projecteuler.net/problem=42

import utilities
import math

def main():
	with open("euler-042-data.txt") as f:
		return len([i for i in [sum([ord(ch) - ord("A") + 1 for ch in word[1:-1]]) for word in f.read().split(",")] if int(math.floor(math.sqrt(i*2)) * math.floor(math.sqrt(i*2) + 1)) == i*2])

if __name__ == "__main__":
	utilities.print_runtime(main)