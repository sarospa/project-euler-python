# Regression tester to verify all solutions still work.

import importlib
import time
import utilities

tests = []
with open("test-data.txt") as f:
	for line in f.readlines():
		dataline = []
		for val in line.split():
			dataline.append(val)
		tests.append(dataline)
all_pass = True
for test in tests:
	utilities.reset()
	solution = importlib.import_module("euler-" + str(test[0]))
	start_time = time.perf_counter()
	result = solution.main()
	runtime = time.perf_counter() - start_time
	test.append(runtime)
	if str(result) == test[1]:
		outcome = "PASS - took %.3f seconds" % runtime
	else:
		outcome = ("FAIL - expected %s, got %s" % (test[1], str(result)))
		all_pass = False
	print("Problem " + test[0] + ": " + outcome)
if all_pass:
	average_runtime = sum([test[2] for test in tests]) / len(tests)
	print("Average runtime: %.3f seconds" % average_runtime)
	slowest_tests = sorted([test for test in tests if test[2] > average_runtime], key=lambda test: test[2], reverse=True)
	print("Slow solutions:")
	for test in slowest_tests:
		print("%s in %.3f seconds" % (test[0], test[2]))
else:
	print("Cannot perform runtime analysis until all tests pass.")