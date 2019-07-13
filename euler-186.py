# Solution to https://projecteuler.net/problem=186

import utilities as utils

PM_NUMBER = 524287
MAX = 1000000

lagged_fib_cache = [0]

def lagged_fibonacci(n):
	while n > 0:
		n -= 1
		k = len(lagged_fib_cache)
		if k <= 55:
			lagged_fib_cache.append((100003 - 200003*k + 300007*k**3) % 1000000)
		else:
			lagged_fib_cache.append((lagged_fib_cache[k - 24] + lagged_fib_cache[k - 55]) % 1000000)

def find_call_group(groups, n):
	val = n
	while groups[val] != val:
		val = groups[val]
	m = n
	while groups[m] != val:
		next_m = groups[m]
		groups[m] = val
		m = next_m
	return val

def main():
	group_counts = [1] * MAX
	groups = {i:i for i in range(MAX)}
	call_index = 1
	call_count = 0
	while group_counts[find_call_group(groups, PM_NUMBER)] < MAX // 100 * 99:
		lagged_fibonacci(2)
		caller = lagged_fib_cache[call_index] % MAX
		called = lagged_fib_cache[call_index + 1] % MAX
		call_index += 2
		if caller != called:
			call_count += 1
			caller_group = find_call_group(groups, caller)
			called_group = find_call_group(groups, called)
			if caller_group != called_group:
				group_counts[caller_group] += group_counts[called_group]
				group_counts[called_group] = 0
				groups[called_group] = caller_group
	return call_count

if __name__ == "__main__":
	utils.print_runtime(main)