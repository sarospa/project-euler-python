# Solution to https://projecteuler.net/problem=3
# Outputs the prime factors from smallest to largest
# Thus, the final factor is the solution.

term = 600851475143
p = 2
while term > p:
	while term % p == 0:
		term = int(term / p)
		print(p)
	p = p + 1
print(term)