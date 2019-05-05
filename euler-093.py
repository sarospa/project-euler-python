# Solution to https://projecteuler.net/problem=93

import fractions
import itertools
import operator
import utilities

ops = [operator.add, operator.sub, operator.mul, fractions.Fraction]

def generate_targets(nums):
	targets = set()
	for i in range(len(nums) - 1):
		for op in ops:
			try:
				new_nums = nums[:i] + (op(nums[i], nums[i+1]),) + nums[i+2:]
				if len(new_nums) == 1:
					targets.add(new_nums[0])
				else:
					targets |= generate_targets(new_nums)
			except:
				pass
	return targets

def main():
	best_target = 0
	best_digits = ""
	for combo in itertools.combinations((1, 2, 3, 4, 5, 6, 7, 8, 9), 4):
		perms = list(itertools.permutations(combo))
		targets = set(itertools.chain.from_iterable([{int(target) for target in generate_targets(perm) if target > 0 and int(target) == target} for perm in perms]))
		for i in itertools.count(1):
			if i not in targets:
				break
			elif i > best_target:
				best_target = i
				best_digits = ''.join([str(num) for num in sorted(combo)])
	return best_digits

if __name__ == "__main__":
	utilities.print_runtime(main)