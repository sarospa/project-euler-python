# Solution to https://projecteuler.net/problem=37

import utilities
import itertools

def main():
	utilities.generate_primes_sieve(1000000)
	prime_set = {str(p) for p in utilities.primes}
	single_digit_primes = {p for p in prime_set if len(p) == 1}
	left_truncatables = {''.join(p) for p in itertools.product("123456789", single_digit_primes)} & prime_set
	right_truncatables = {''.join(p) for p in itertools.product(single_digit_primes, "123456789")} & prime_set
	for i in range(6):
		left_truncatables |= {''.join(p) for p in itertools.product("123456789", left_truncatables)} & prime_set
		right_truncatables |= {''.join(p) for p in itertools.product(right_truncatables, "123456789")} & prime_set
	return sum({int(p) for p in left_truncatables & right_truncatables})
		

if __name__ == "__main__":
	utilities.print_runtime(main)