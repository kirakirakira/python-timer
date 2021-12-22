from adafruit_circuitplayground import cp
import time
from timer_collection import TimerCollection

cp.pixels.brightness = 0.01

clear = (0, 0, 0)
pink = (250, 50, 174)
blue = (0, 0, 255)
green = (0, 255, 0)
red = (255, 0, 0)
teal = (0, 255, 255)
yellow = (255, 255, 0)
orange = (255, 30, 30)


timer_collection = TimerCollection()

cp.red_led = False

for pixel in range(10):
    cp.pixels[pixel] = clear

def red_led_callback():
    cp.red_led = not cp.red_led

def pixel_callback(*args):
    index = args[0][0]
    color = args[0][1]

    if cp.pixels[index] == clear:
        cp.pixels[index] = color
    else:
        cp.pixels[index] = clear

timer_collection.start_periodic_timer(1, red_led_callback)

timer_configs = [
    {"interval": 0.2, "led": (0, pink)},
    {"interval": 0.3, "led": (1, blue)},
    {"interval": 0.4, "led": (2, yellow)},
    {"interval": 0.5, "led": (3, red)},
    {"interval": 0.6, "led": (4, teal)},
    {"interval": 0.5, "led": (5, orange)},
    {"interval": 0.4, "led": (6, blue)},
    {"interval": 0.3, "led": (7, pink)},
    {"interval": 0.2, "led": (8, green)},
    {"interval": 0.6, "led": (9, red)}
]

christmas_configs = [
    {"interval": 0.2, "led": (0, red)},
    {"interval": 0.3, "led": (1, green)},
    {"interval": 0.4, "led": (2, red)},
    {"interval": 0.5, "led": (3, green)},
    {"interval": 0.6, "led": (4, red)},
    {"interval": 0.5, "led": (5, green)},
    {"interval": 0.4, "led": (6, red)},
    {"interval": 0.3, "led": (7, green)},
    {"interval": 0.2, "led": (8, red)},
    {"interval": 0.6, "led": (9, green)}
]

for timer_config in christmas_configs:
    timer_collection.start_periodic_timer(
        timer_config["interval"],
        pixel_callback,
        timer_config["led"]
    )

while True:
    time_until_next = timer_collection.run()

    if time_until_next != None:
        time.sleep(time_until_next)
    else:
        time.sleep(1)
