# Solution to 

import utilities

def main():
	return sum([i**i for i in range(1, 1001)]) % 10**10

if __name__ == "__main__":
	utilities.print_runtime(main)