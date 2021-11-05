import time


class TimerCollection(object):

    class Timer(object):
        def __init__(self, interval, fn):
            self.interval = interval
            self._fn = fn

        @property
        def remaining_ticks(self):
            # elapsed_timer = time.monotonic() - self._start_time
            # return self._interval - elapsed_time
            return self.interval

    def __init__(self) -> None:
        super().__init__()
        self.timers = []

    def add_timer(self, interval, fn):
        timer = self.Timer(interval, fn)
        self.timers.append(timer)
        return timer

    def start_timer(self, interval, fn):
        return self.add_timer(interval, fn)
