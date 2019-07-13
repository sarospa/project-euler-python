# Solution to https://projecteuler.net/problem=151

import utilities as utils

def main():
	outcomes = []
	outcomes.append(dict())
	outcomes[0][(1, 0, 0, 0, 0)] = (1.0, 0.0)
	while len(outcomes) < 16:
		outcomes.append(dict())
		for outcome in outcomes[len(outcomes) - 2]:
			total_paper = sum(outcome)
			for i in range(5):
				if outcome[i] > 0:
					next_outcome = list(outcome)
					next_outcome[i] -= 1
					for j in range(i + 1, 5):
						next_outcome[j] += 1
					next_outcome = tuple(next_outcome)
					weight = outcomes[len(outcomes) - 2][outcome][0] * (outcome[i] / total_paper)
					expected = outcomes[len(outcomes) - 2][outcome][1] * (outcome[i] / total_paper)
					if sum(next_outcome) == 1:
						expected += weight
					values = (0.0, 0.0)
					if next_outcome in outcomes[len(outcomes) - 1]:
						values = outcomes[len(outcomes) - 1][next_outcome]
					outcomes[len(outcomes) - 1][next_outcome] = (weight + values[0], expected + values[1])
	expected_value = outcomes[len(outcomes) - 1][(0, 0, 0, 0, 1)][1] - 1
	return round(expected_value, 6)

if __name__ == "__main__":
	utils.print_runtime(main)