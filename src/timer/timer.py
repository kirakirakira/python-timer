import time


class Timer(object):
    _STOPPED = 'STOPPED'
    _RUNNING = 'RUNNING'
    
    def __init__(self, interval, fn):
        self._fn = fn
        self._interval = interval
        self._status = Timer._STOPPED
        # self._callback = callback
        self.finished = False

    @property
    def status(self):
        return self._status

    def start(self):
        self._start_time = time.monotonic()
    
    @property
    def remaining_ticks(self):
        elapsed_time = time.monotonic() - self._start_time
        # print("inside remaining ticks", elapsed_time)
        # make sure remaining ticks doesn't go negative
        return self._interval - elapsed_time

    def run(self):
        # print("inside run", self.remaining_ticks)
        # while self.remaining_ticks > 0:
        #     if self.remaining_ticks == 0:
        #         break
        if self.remaining_ticks == 0:
            self.finished = True
            self._fn()
