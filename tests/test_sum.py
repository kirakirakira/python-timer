import unittest
from fractions import Fraction
from src.sum.sum import sum


class TestSum(unittest.TestCase):
    def test_list_integers(self):
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_list_floats(self):
        data = [1.2, 3.24, 3.0]
        result = sum(data)
        self.assertAlmostEqual(result, 7.44, 2)

    def test_list_fractions(self):
        data = [Fraction(1,4), Fraction(1,4), Fraction(2,5)]
        result = sum(data)
        self.assertEqual(result, Fraction(9, 10))

if __name__ == '__main__':
    unittest.main()