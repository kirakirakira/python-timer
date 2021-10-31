class Timer(object):
    _STOPPED = 'STOPPED'
    _RUNNING = 'RUNNING'
    
    def __init__(self, interval):
        self._interval = interval
        self._status = Timer._STOPPED
        self._start_time = 0

    @property
    def status(self):
        return self._status