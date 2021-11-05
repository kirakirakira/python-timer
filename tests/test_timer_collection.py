import unittest
from src.timer.timer_collection import TimerCollection
from unittest import mock
from tests.time_mock import Time_Mock

timey = Time_Mock()

class TestTimerCollection(unittest.TestCase):
    def test_init(self):
        new_timer_collection = TimerCollection()

    def test_start_timer(self):
        new_timer_collection = TimerCollection()
        new_timer_collection.start_timer(5, lambda: True)

    @mock.patch('time.monotonic', timey.current_time)
    def test_remaining_ticks(self):
        new_timer_collection = TimerCollection()
        timer = new_timer_collection.start_timer(5, lambda: True)
        self.assertEqual(timer.remaining_ticks, 5)

    @mock.patch('time.monotonic', timey.current_time)
    def test_elapse_time(self):
        new_timer_collection = TimerCollection()
        timer = new_timer_collection.start_timer(5, lambda: True)
        self.assertEqual(timer.remaining_ticks, 5)
        timey.elapse(1)
        self.assertEqual(timer.remaining_ticks, 4)

    @mock.patch('time.monotonic', timey.current_time)
    def test_run_to_complete(self):
        called_back = [False]

        def callback():
            called_back[0] = True

        new_timer_collection = TimerCollection()
        timer = new_timer_collection.start_timer(5, callback)
        self.assertEqual(timer.remaining_ticks, 5)
        timey.elapse(5)
        new_timer_collection.run()
        self.assertEqual(called_back[0], True)

if __name__ == '__main__':
    unittest.main()
