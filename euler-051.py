# Solution to https://projecteuler.net/problem=51

import itertools
import utilities

digits = "0123456789"

def main():
	utilities.generate_primes_sieve(1000000)
	prime_set = set(utilities.primes)
	templates = [''.join(num) for num in list(itertools.product(digits, digits, digits, "*", "*", "*"))+ list(itertools.product(digits, digits, "*", "*", "*")) + list(itertools.product(digits, "*", "*", "*"))]
	templates = [''.join(item) for sublist in [set(itertools.permutations(template)) for template in templates] for item in sublist]
	for template in templates:
		prime_family = [p for p in [int(template.replace("*", digit)) for digit in digits] if p in prime_set and len(str(p)) == len(template)]
		if len(prime_family) >= 8:
			return int(min(prime_family))

if __name__ == "__main__":
	utilities.print_runtime(main)