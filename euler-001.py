# Solution to https://projecteuler.net/problem=1

n = 0
for i in range(1, 1000):
	if i % 3 == 0 or i % 5 == 0:
		n = n + i
print(n)