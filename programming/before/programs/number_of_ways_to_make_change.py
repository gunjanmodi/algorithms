import unittest

def number_of_ways_to_make_change(n, denoms):
    ways = [0 for i in range(n + 1)]
    ways[0] = 1
    for denom in denoms:
        for amount in range(1, n + 1):
            if denom <= amount:
                ways[amount] += ways[amount - denom]
    return ways[n] 

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        num_of_ways = number_of_ways_to_make_change(10, [1, 5, 10, 25])
        self.assertEqual(num_of_ways, 4)

if __name__ == '__main__':
    unittest.main()