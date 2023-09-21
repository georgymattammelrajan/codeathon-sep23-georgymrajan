import unittest
from program2 import max_profit

class TestMaxProfit(unittest.TestCase):
    def test_max_profit(self):
        # Test case 1
        prices = [7, 1, 5, 3, 6, 4]
        self.assertEqual(max_profit(prices), 5)

        # Test case 2
        prices = [7, 6, 4, 3, 1]
        self.assertEqual(max_profit(prices), -1)

        # Test case 3
        prices = [2, 4, 1]
        self.assertEqual(max_profit(prices), 2)

        # Test case 4
        prices = [2, 1, 2, 1, 0, 1, 2]
        self.assertEqual(max_profit(prices), 2)

        # Test case 5
        prices = [1, 2, 3, 4, 5]
        self.assertEqual(max_profit(prices), 4)

if __name__ == '__main__':
    unittest.main()