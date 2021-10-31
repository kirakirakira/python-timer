import unittest
from src.timer.timer import Timer


class TestTimer(unittest.TestCase):
    def test_init(self):
        new_timer = Timer(5)
        self.assertEqual(new_timer.status, Timer._STOPPED)

    def test_start(self):
        new_timer = Timer(5)
        new_timer.start()
        self.assertEqual(new_timer.remaining_ticks, 5)

if __name__ == '__main__':
    unittest.main()