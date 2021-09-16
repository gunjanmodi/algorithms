import unittest
# O(nc) time | O(nc) space
def knapsack(items, capacity):
    knapsack_values = [[0 for x in range(capacity + 1)] for y in range(len(items) + 1)]
    for i in range(1, len(items) + 1):
        current_value = items[i - 1][0]
        current_weight = items[i - 1][1]
        for c in range(0, capacity + 1):
            if current_weight > c:
                knapsack_values[i][c] = knapsack_values[i - 1][c]
            else:
                knapsack_values[i][c] = max(
                    knapsack_values[i - 1][c],
                    knapsack_values[i - 1][c - current_weight] + current_value
                )
    return knapsack_values

def get_knapsack_values(items, knapsack_values):
    sequence = []
    i = len(knapsack_values) - 1
    c = len(knapsack_values[0]) - 1
    while i > 0:
        if knapsack_values[i][c] == knapsack_values[i - 1][c]:
            i -= 1
        else:
            sequence.append(i - 1)
            c -= items[i - 1][1]
            i -= 1
        if c == 0:
            break
    return list(reversed(sequence))


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(knapsack([[1, 2], [4, 3], [5, 6], [6, 7]], 10), [10, [1, 3]])


if __name__ == '__main__':
    unittest.main()