from adafruit_circuitplayground import cp
import time
from timer_collection import TimerCollection

cp.pixels.brightness = 0.01
clear = (0, 0, 0)
pink = (250, 50, 174)

steps = [0]
timer_collection = TimerCollection()

cp.red_led = False

def clear_all_pixels():
    for pixel in range(10):
        cp.pixels[pixel] = clear

def light_up_pixels(index):
    for pixel in range(index):
        cp.pixels[pixel] = pink

def red_led_callback():
    cp.red_led = not cp.red_led

def button_callback():
    if cp.button_a:
        multiplier = steps[0] // 10
        light_up_pixels(multiplier)
    else:
        clear_all_pixels()

def step_counter():
    steps[0] += 1
    print(steps[0])

clear_all_pixels()

timer_collection.start_periodic_timer(1, red_led_callback)
timer_collection.start_periodic_timer(0.1, button_callback)
timer_collection.start_periodic_timer(1, step_counter)

while True:
    time_until_next = timer_collection.run()

    if time_until_next != None:
        time.sleep(time_until_next)
    else:
        time.sleep(1)
