# Solution to https://projecteuler.net/problem=53

import math
import utilities

def main():
	return len([i for i in [math.factorial(n) // (math.factorial(r) * math.factorial(n - r)) for n in range(1, 101) for r in range(1, n + 1)] if i > 1000000])

if __name__ == "__main__":
	utilities.print_runtime(main)