# Regression tester to verify all solutions still work.

import importlib
import utilities

tests = []
with open("test-data.txt") as f:
	for line in f.readlines():
		dataline = []
		for val in line.split():
			dataline.append(val)
		tests.append(dataline)
for test in tests:
	utilities.reset()
	solution = importlib.import_module("euler-" + str(test[0]))
	result = solution.main()
	if str(result) == test[1]:
		outcome = "PASS"
	else:
		outcome = ("FAIL - expected %s, got %s" % (test[1], str(result)))
	print("Problem " + test[0] + ": " + outcome)