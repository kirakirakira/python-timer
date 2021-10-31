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
        self._start_time = 0
    
    @property
    def remaining_ticks(self):
        return self._interval - self._start_time