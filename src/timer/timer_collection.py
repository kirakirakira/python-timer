import time
import sys


class TimerCollection(object):

    class Timer(object):
        def __init__(self, timer_collection, interval, fn, argument = None, periodic = False):
            self._start_time = time.monotonic()
            self._interval = interval
            self._fn = fn
            self._argument = argument
            self._periodic = periodic
            self._timer_collection = timer_collection

        @property
        def remaining_ticks(self):
            elapsed_time = time.monotonic() - self._start_time
            remaining_ticks = self._interval - elapsed_time
            return remaining_ticks if remaining_ticks >= 0 else 0

        def stop(self):
            self._timer_collection.timers.remove(self)


    def __init__(self):
        self.timers = []
        self.last_ticks = time.monotonic()

    def _add_timer(self, interval, fn, argument = None, periodic = False):
        timer = self.Timer(self, interval, fn, argument, periodic)
        self.timers.append(timer)
        return timer

    def start_timer(self, interval, fn, argument = None):
        return self._add_timer(interval, fn, argument)

    def start_periodic_timer(self, interval, fn, argument = None):
        return self._add_timer(interval, fn, argument, periodic = True)

    def run(self):
        timers_to_remove = []

        next_ready = float('inf')
        did_one = False

        for timer in self.timers:
            if not did_one and timer.remaining_ticks == 0:
                did_one = True

                if timer._argument != None:
                    timer._fn(timer._argument)
                else:
                    timer._fn()

                if not timer._periodic:
                    timers_to_remove.append(timer)
                else:
                    timer._start_time = time.monotonic()
                    next_ready = min(next_ready, timer.remaining_ticks)
            else:
                next_ready = min(next_ready, timer.remaining_ticks)

        for timer in timers_to_remove:
            self.timers.remove(timer)

        return next_ready if next_ready != float('inf') else None
