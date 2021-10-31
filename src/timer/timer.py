import time


class Timer(object):
    _STOPPED = 'STOPPED'
    _RUNNING = 'RUNNING'
    
    def __init__(self, interval):
        self._interval = interval
        self._status = Timer._STOPPED

    @property
    def status(self):
        return self._status

    def start(self):
        self._start_time = time.monotonic()
    
    @property
    def remaining_ticks(self):
        elapsed_time = time.monotonic() - self._start_time
        return self._interval - elapsed_time
