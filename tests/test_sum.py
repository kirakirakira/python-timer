import unittest
from src.sum.sum import sum


class TestSum(unittest.TestCase):
    def test_list_integers(self):
        data = [1, 2, 3]
        print(sum(data))
        result = sum(data)
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()