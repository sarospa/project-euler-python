# Solution to https://projecteuler.net/problem=29

import utilities

def main():
	return len({a ** b for a in range(2, 101) for b in range(2, 101)})

if __name__ == "__main__":
	utilities.print_runtime(main)