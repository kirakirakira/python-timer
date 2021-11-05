class Time_Mock(object):
    def __init__(self):
        self._current_time = 0

    def elapse(self, seconds):
        self._current_time += seconds

    def current_time(self):
        return self._current_time

# def main():
#     # inits

#     while True:
#         time_until_next = timer_thing.run()
#         os.sleep(time_until_next)



# my_timer = timer_thing.start_timer(5, lambda: True)
# my_timer.remaining_ticks
# my_timer.stop()
# my_timer = timer_thing.start(...)
