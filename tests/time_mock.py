class Time_Mock(object):
    def __init__(self):
        self._current_time = 0

    def elapse(self, seconds):
        self._current_time += seconds

    def current_time(self):
        return self._current_time
