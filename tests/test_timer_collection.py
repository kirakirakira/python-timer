import unittest
from src.timer.timer_collection import TimerCollection
from unittest import mock
from tests.time_mock import Time_Mock

timey = Time_Mock()

class TestTimerCollection(unittest.TestCase):
    def test_init(self):
        new_timer_collection = TimerCollection()

    # def test_add_timer(self):
    #     new_timer_collection = TimerCollection()
    #     new_timer_collection.add_timer(5, lambda: True)

    def test_start_timer(self):
        new_timer_collection = TimerCollection()
        new_timer_collection.start_timer(5, lambda: True)

if __name__ == '__main__':
    unittest.main()
