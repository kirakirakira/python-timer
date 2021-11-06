import time


class TimerCollection(object):

    class Timer(object):
        def __init__(self, interval, fn):
            self._start_time = time.monotonic()
            self._interval = interval
            self._fn = fn

        @property
        def remaining_ticks(self):
            # need to make sure not less than 0
            elapsed_time = time.monotonic() - self._start_time
            remaining_ticks = self._interval - elapsed_time

            if remaining_ticks < 0:
                return 0
            else:
                return remaining_ticks

    def __init__(self):
        self.timers = []

    def _add_timer(self, interval, fn):
        timer = self.Timer(interval, fn)
        self.timers.append(timer)
        return timer

    def start_timer(self, interval, fn):
        return self._add_timer(interval, fn)

    def run(self):
        timers_to_remove = []
        for timer in self.timers:
            if timer.remaining_ticks == 0:
                timer._fn()
                timers_to_remove.append(timer)
        
        for timer in timers_to_remove:
            self.timers.remove(timer)
