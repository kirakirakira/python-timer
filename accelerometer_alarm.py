from adafruit_circuitplayground import cp
import time
from timer_collection import TimerCollection

# Hardware setup
cp.pixels.brightness = 0.01

# Constants
DEBOUNCE_COUNT = 5
CYCLE_COMPLETE_DELAY_TIME_IN_SECONDS = 5
HEARTBEAT_LED_PERIOD_IN_SECONDS = 0.2
ACCELEROMETER_MONITOR_PERIOD_IN_SECONDS = 2
ACCELERATION_DIFFERENCE_THRESHOLD = 0.5

# Initialization
previous_acceleration = {"x": cp.acceleration.x, "y": cp.acceleration.y, "z": cp.acceleration.z}
acceleration = {"x": cp.acceleration.x, "y": cp.acceleration.y, "z": cp.acceleration.z}
difference = {"delta x": 0, "delta y": 0, "delta z": 0}

timer_collection = TimerCollection()

acceleration_monitor_timer = [None]
acceleration_monitor_limit = [0]
debounce = [0]

def reset_accelerometer_monitor_limit():
    acceleration_monitor_limit[0] = 0

def start_accelerometer_monitoring():
    acceleration_monitor_limit[0] += 1

    if acceleration_monitor_limit[0] == 1:
        debounce[0] = 0
        acceleration_monitor_timer[0] = timer_collection.start_periodic_timer(2, print_acceleration)

def blink_led():
    cp.red_led = not cp.red_led

def cycle_complete():
    cp.play_file("burp_x.wav")
    reset_accelerometer_monitor_limit()
    print("YOU ARE DONE")

def print_acceleration():
    # print(debounce[0])
    # print(acceleration_monitor_limit[0])

    acceleration = {"x": cp.acceleration.x, "y": cp.acceleration.y, "z": cp.acceleration.z}
    difference["delta x"] = abs(acceleration["x"] - previous_acceleration["x"])
    difference["delta y"] = abs(acceleration["y"] - previous_acceleration["y"])
    difference["delta z"] = abs(acceleration["z"] - previous_acceleration["z"])

    # print("current ", acceleration) 
    # print("previous", previous_acceleration)
    # print("difference", difference)

    if difference["delta x"] < ACCELERATION_DIFFERENCE_THRESHOLD and \
        difference["delta y"] < ACCELERATION_DIFFERENCE_THRESHOLD and \
        difference["delta z"] < ACCELERATION_DIFFERENCE_THRESHOLD:
        print("DIFFERENCE IS LOW ENOUGH")
        debounce[0] += 1
    else:
        debounce[0] = 0

    if debounce[0] >= DEBOUNCE_COUNT:
        acceleration_monitor_timer[0].stop()
        timer_collection.start_timer(CYCLE_COMPLETE_DELAY_TIME_IN_SECONDS, cycle_complete)

    previous_acceleration["x"] = acceleration["x"]
    previous_acceleration["y"] = acceleration["y"]
    previous_acceleration["z"] = acceleration["z"]

timer_collection.start_periodic_timer(HEARTBEAT_LED_PERIOD_IN_SECONDS, blink_led)
acceleration_monitor_timer[0] = timer_collection.start_periodic_timer(ACCELEROMETER_MONITOR_PERIOD_IN_SECONDS, print_acceleration)


while True:
    time_until_next = timer_collection.run()

    if cp.button_a:
        start_accelerometer_monitoring()

    if time_until_next != None:
        time.sleep(time_until_next)
    else:
        time.sleep(1)
