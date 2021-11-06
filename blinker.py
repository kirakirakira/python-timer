# from adafruit_circuitplayground import cp
import time
from src.timer.timer_collection import TimerCollection

timer_collection = TimerCollection()

called_back = [False]

def callback():
    called_back[0] = True
    print(called_back[0])

timer = timer_collection.start_timer(5, callback)

while True:
    time_until_next = timer_collection.run()

    if time_until_next != None:
        time.sleep(time_until_next)
    else:
        time.sleep(1)
