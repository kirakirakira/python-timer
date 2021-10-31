import time


class Timer(object):
    _STOPPED = 'STOPPED'
    _RUNNING = 'RUNNING'
    
    def __init__(self, interval):
        self._interval = interval
        self._status = Timer._STOPPED
        # self._callback = callback
        self.finished = False

    @property
    def status(self):
        return self._status

    def start(self):
        self._start_time = time.monotonic()
    
    @property # not use a property?
    def remaining_ticks(self):
        # need to make the mock update time.monotonic in here
        elapsed_time = time.monotonic() - self._start_time
        print("inside remaining ticks", elapsed_time)
        if(self._interval - elapsed_time == 0):
            self._finished = True
        return self._interval - elapsed_time

    def run(self):
        print("inside run", self.remaining_ticks)
        while self.remaining_ticks > 0:
            if self.remaining_ticks == 0:
                break
        self._finished = True
