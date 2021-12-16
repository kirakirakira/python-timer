from adafruit_circuitplayground import cp
import time
from timer_collection import TimerCollection

cp.pixels.brightness = 0.01

previous_acceleration = {"x": cp.acceleration.x, "y": cp.acceleration.y, "z": cp.acceleration.z}
acceleration = {"x": cp.acceleration.x, "y": cp.acceleration.y, "z": cp.acceleration.z}
difference = {"delta x": 0, "delta y": 0, "delta z": 0}

timer_collection = TimerCollection()

acceleration_monitor_timer = [None]
acceleration_monitor_limit = [0]
debounce = [0]

def blink_led():
    cp.red_led = not cp.red_led

def youre_done():
    cp.play_file("burp_x.wav")
    acceleration_monitor_limit[0] = 0
    print("YOU ARE DONE")

def print_acceleration():
    print(debounce[0])
    print(acceleration_monitor_limit[0])

    acceleration = {"x": cp.acceleration.x, "y": cp.acceleration.y, "z": cp.acceleration.z}
    difference["delta x"] = abs(acceleration["x"] - previous_acceleration["x"])
    difference["delta y"] = abs(acceleration["y"] - previous_acceleration["y"])
    difference["delta z"] = abs(acceleration["z"] - previous_acceleration["z"])

    print("current ", acceleration) 
    print("previous", previous_acceleration)
    print("difference", difference)

    if difference["delta x"] < 0.5 and difference["delta y"] < 0.5 and difference["delta z"] < 0.5:
        print("DIFFERENCE IS LOW ENOUGH")
        debounce[0] += 1
    else:
        debounce[0] = 0

    if debounce[0] >= 5:
        timer_collection.stop(acceleration_monitor_timer[0])
        timer_collection.start_timer(5, youre_done)

    previous_acceleration["x"] = acceleration["x"]
    previous_acceleration["y"] = acceleration["y"]
    previous_acceleration["z"] = acceleration["z"]

blink_led_timer = timer_collection.start_periodic_timer(0.2, blink_led)
acceleration_monitor_timer[0] = timer_collection.start_periodic_timer(2, print_acceleration)


while True:
    time_until_next = timer_collection.run()

    if cp.button_a:
        acceleration_monitor_limit[0] += 1

        if acceleration_monitor_limit[0] == 1:
            debounce[0] = 0
            acceleration_monitor_timer[0] = timer_collection.start_periodic_timer(2, print_acceleration)

    if time_until_next != None:
        time.sleep(time_until_next)
    else:
        time.sleep(1)
