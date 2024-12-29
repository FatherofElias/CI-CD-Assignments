import unittest


class TestSumFunction(unittest.TestCase):
    def test_negative_sum(self):
        result = sum_function(-1, -1)
        self.assertEqual(result, -2)

if __name__ == '__main__':
    unittest.main()
