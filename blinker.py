from adafruit_circuitplayground import cp
import time
from timer_collection import TimerCollection

cp.pixels.brightness = 0.01

pink = (250, 50, 174)
blue = (0, 0, 255)
green = (0, 255, 0)
clear = (0, 0, 0)

timer_collection = TimerCollection()

cp.red_led = False
cp.pixels[0] = clear
cp.pixels[1] = clear
cp.pixels[2] = clear

def red_led_callback():
    cp.red_led = not cp.red_led
    print(cp.red_led)

def pixel_callback(*args):
    index = args[0][0]
    color = args[0][1]

    if cp.pixels[index] == clear:
        cp.pixels[index] = color
    else:
        cp.pixels[index] = clear

timer_red_led = timer_collection.start_periodic_timer(1, red_led_callback)
timer_pixel_0 = timer_collection.start_periodic_timer(2, pixel_callback, (0, pink))
timer_pixel_1 = timer_collection.start_periodic_timer(3, pixel_callback, (1, blue))
timer_pixel_2 = timer_collection.start_periodic_timer(4, pixel_callback, (2, green))

while True:
    time_until_next = timer_collection.run()

    if time_until_next != None:
        time.sleep(time_until_next)
    else:
        time.sleep(1)
