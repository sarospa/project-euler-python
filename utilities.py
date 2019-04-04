import time

def is_palindrome(val):
	str_val = str(val)
	for i in range(0, len(str_val) // 2):
		if str_val[i] != str_val[-(i + 1)]:
			return False
	return True

def print_runtime(func):
	start_time = time.perf_counter()
	func()
	runtime = time.perf_counter() - start_time
	print("Solved in %.3f seconds." % runtime)