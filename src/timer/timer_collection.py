import time


class TimerCollection(object):

    class Timer(object):
        def __init__(self, interval, fn):
            self.interval = interval
            self._fn = fn

    def __init__(self) -> None:
        super().__init__()
        self.timers = []

    def add_timer(self, interval, fn):
        self.timers.append(self.Timer(interval, fn))

    def start_timer(self, interval, fn):
        self.add_timer(interval, fn)
