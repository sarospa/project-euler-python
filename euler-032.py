# Solution to https://projecteuler.net/problem=32

import utilities

def main():
	products = set()
	for i in range(2, 5000):
		for j in range(2, 10000 // i):
			product = i * j
			if ''.join(sorted(str(i) + str(j) + str(product))) == "123456789":
				products.add(product)
	return sum(products)

if __name__ == "__main__":
	utilities.print_runtime(main)