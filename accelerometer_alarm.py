from adafruit_circuitplayground import cp
import time
from timer_collection import TimerCollection

cp.pixels.brightness = 0.01

previous_acceleration = {"x": cp.acceleration.x, "y": cp.acceleration.y, "z": cp.acceleration.z}
acceleration = {"x": cp.acceleration.x, "y": cp.acceleration.y, "z": cp.acceleration.z}
difference = {"delta x": 0, "delta y": 0, "delta z": 0}

timer_collection = TimerCollection()

acceleration_monitor_timer = [None]

def blink_led():
    cp.red_led = not cp.red_led

def youre_done():
    cp.play_file("burp_x.wav")
    button_pressed = 0
    print("YOU ARE DONE 1347183O4134")

def print_acceleration():
    acceleration = {"x": cp.acceleration.x, "y": cp.acceleration.y, "z": cp.acceleration.z}
    difference["delta x"] = abs(acceleration["x"] - previous_acceleration["x"])
    difference["delta y"] = abs(acceleration["y"] - previous_acceleration["y"])
    difference["delta z"] = abs(acceleration["z"] - previous_acceleration["z"])

    print("current ", acceleration) 
    print("previous", previous_acceleration)
    print("difference", difference)

    if difference["delta x"] < 0.5 and difference["delta y"] < 0.5 and difference["delta z"] < 0.5:
        print("YOU ARE THE BESTEST **********")
        print(acceleration_monitor_timer[0])
        timer_collection.stop(acceleration_monitor_timer[0])
        timer_collection.start_timer(5, youre_done)
    previous_acceleration["x"] = acceleration["x"]
    previous_acceleration["y"] = acceleration["y"]
    previous_acceleration["z"] = acceleration["z"]

blink_led_timer = timer_collection.start_periodic_timer(0.2, blink_led)
acceleration_monitor_timer[0] = timer_collection.start_periodic_timer(2, print_acceleration)

button_pressed = 0

while True:
    time_until_next = timer_collection.run()

    if cp.button_a:
        print("BUTTON A IS PRESSED =======")
        button_pressed += 1
        print(button_pressed)

        if button_pressed == 1:
            print("A BUTTON TIMER STARTED")
            acceleration_monitor_timer[0] = timer_collection.start_periodic_timer(2, print_acceleration)

    if time_until_next != None:
        time.sleep(time_until_next)
    else:
        time.sleep(1)
