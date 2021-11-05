import unittest
from src.timer.timer import Timer
from unittest import mock
from tests.time_mock import Time_Mock

timey = Time_Mock()

class TestTimer(unittest.TestCase):
    def test_init(self):
        new_timer = Timer(5, lambda: True)
        self.assertEqual(new_timer.status, 'STOPPED')

    @mock.patch('time.monotonic', timey.current_time)
    def test_start(self):
        new_timer = Timer(5, lambda: True)
        new_timer.start()
        self.assertEqual(new_timer.remaining_ticks, 5)

    @mock.patch('time.monotonic', timey.current_time)
    def test_elapse_time(self):
        new_timer = Timer(5, lambda: True)
        new_timer.start()
        timey.elapse(1)
        self.assertEqual(new_timer.remaining_ticks, 4)
        timey.elapse(2)
        self.assertEqual(new_timer.remaining_ticks, 2)

    @mock.patch('time.monotonic', timey.current_time)  # time needs to go by...
    def test_finish_timing(self):
        called_back = [False]

        def callback():
            called_back[0] = True

        new_timer = Timer(5, callback)
        new_timer.start()
        timey.elapse(5)
        new_timer.run()
        self.assertEqual(new_timer.finished, True)
        self.assertEqual(called_back[0], True)

if __name__ == '__main__':
    unittest.main()
