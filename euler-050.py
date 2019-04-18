# Solution to https://projecteuler.net/problem=50

import utilities

MAX = 1000000

def main():
	utilities.generate_primes_sieve(MAX)
	prime_set = set(utilities.primes)
	index = 0
	size = len(utilities.primes)
	while size > 0:
		if size % 10 == 0:
			print((index, size))
		p = sum(utilities.primes[index:index + size])
		if p in prime_set:
			return p
		while p > MAX:
			if index == 0:
				p -= utilities.primes[size - 1]
				if p in prime_set:
					return p
			else:
				index = 0
				p = 0
			size -= 1
		else:
			index += 1

if __name__ == "__main__":
	utilities.print_runtime(main)