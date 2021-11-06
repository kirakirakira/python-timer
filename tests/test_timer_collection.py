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

    @mock.patch('time.monotonic', timey.current_time)
    def test_multiple_timers(self):
        called_back_a = [False]

        def callback_a():
            called_back_a[0] = True

        called_back_b = [False]

        def callback_b():
            called_back_b[0] = True

        new_timer_collection = TimerCollection()
        timer_a = new_timer_collection.start_timer(5, callback_a)
        self.assertEqual(timer_a.remaining_ticks, 5)
        timey.elapse(2)

        timer_b = new_timer_collection.start_timer(3, callback_b)
        self.assertEqual(timer_a.remaining_ticks, 3)
        self.assertEqual(timer_b.remaining_ticks, 3)

        timey.elapse(3)
        new_timer_collection.run()
        self.assertEqual(called_back_a[0], True)
        self.assertEqual(called_back_b[0], True)

    @mock.patch('time.monotonic', timey.current_time)
    def test_remaining_ticks_is_only_positive(self):
        called_back = [False]

        def callback():
            called_back[0] = True

        new_timer_collection = TimerCollection()
        timer = new_timer_collection.start_timer(5, callback)
        self.assertEqual(timer.remaining_ticks, 5)

        timey.elapse(5)
        new_timer_collection.run()
        self.assertEqual(called_back[0], True)
        self.assertEqual(timer.remaining_ticks, 0)

        timey.elapse(1)
        self.assertEqual(timer.remaining_ticks, 0)

    @mock.patch('time.monotonic', timey.current_time)
    def test_remove_finished_timer_from_list(self):
        called_back = [0]

        def callback():
            called_back[0] += 1

        new_timer_collection = TimerCollection()
        timer = new_timer_collection.start_timer(5, callback)
        self.assertEqual(timer.remaining_ticks, 5)

        timey.elapse(5)
        new_timer_collection.run()
        self.assertEqual(called_back[0], 1)

        timey.elapse(5)
        new_timer_collection.run()
        self.assertEqual(called_back[0], 1)

    @mock.patch('time.monotonic', timey.current_time)
    def test_multiple_timers_that_finish_at_different_times(self):
        called_back_a = [0]

        def callback_a():
            called_back_a[0] += 1

        called_back_b = [0]

        def callback_b():
            called_back_b[0] += 1

        new_timer_collection = TimerCollection()
        timer_a = new_timer_collection.start_timer(6, callback_a)
        self.assertEqual(timer_a.remaining_ticks, 6)
        timey.elapse(2)

        timer_b = new_timer_collection.start_timer(3, callback_b)
        self.assertEqual(timer_a.remaining_ticks, 4)
        self.assertEqual(timer_b.remaining_ticks, 3)

        timey.elapse(3)
        new_timer_collection.run()
        self.assertEqual(called_back_b[0], 1)

        timey.elapse(1)
        new_timer_collection.run()
        self.assertEqual(called_back_a[0], 1)

        timey.elapse(6)
        self.assertEqual(called_back_a[0], 1)
        self.assertEqual(called_back_b[0], 1)

    @mock.patch('time.monotonic', timey.current_time)
    def test_periodic_timer(self):
        called_back = [0]

        def callback():
            called_back[0] += 1

        new_timer_collection = TimerCollection()
        timer = new_timer_collection.start_periodic_timer(5, callback)
        self.assertEqual(timer.remaining_ticks, 5)

        timey.elapse(5)
        new_timer_collection.run()
        self.assertEqual(called_back[0], 1)

        timey.elapse(5)
        new_timer_collection.run()
        self.assertEqual(called_back[0], 2)

        timey.elapse(5)
        new_timer_collection.run()
        self.assertEqual(called_back[0], 3)


if __name__ == '__main__':
    unittest.main()
