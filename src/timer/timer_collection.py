import time


class TimerCollection(object):

    class Timer(object):
        def __init__(self, interval, fn, periodic = False):
            self._start_time = time.monotonic()
            self._interval = interval
            self._fn = fn
            self._periodic = periodic

        @property
        def remaining_ticks(self):
            elapsed_time = time.monotonic() - self._start_time
            remaining_ticks = self._interval - elapsed_time
            return remaining_ticks if remaining_ticks >= 0 else 0

    def __init__(self):
        self.timers = []

    def _add_timer(self, interval, fn, periodic = False):
        timer = self.Timer(interval, fn, periodic)
        self.timers.append(timer)
        return timer

    def start_timer(self, interval, fn):
        return self._add_timer(interval, fn)

    def start_periodic_timer(self, interval, fn):
        return self._add_timer(interval, fn, periodic = True)

    def run(self):
        timers_to_remove = []
        for timer in self.timers:
            if timer.remaining_ticks == 0:
                timer._fn()
                if not timer._periodic:
                    timers_to_remove.append(timer)
        
        for timer in timers_to_remove:
            self.timers.remove(timer)
