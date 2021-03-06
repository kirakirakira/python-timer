# Non-blocking timer in CircuitPython and Accelerometer Alarm Application

#### Description:
This accelerometer alarm uses CircuitPython and the Circuit Playground Bluefruit's on board accelerometer to monitor for changes in acceleration. Once the change in acceleration in x, y, and z directions no longer changes more than 0.5 m/s^2 for X number of debounce times (set to 5 in code currently), then it will delay for X seconds (set to 5 in the code currently). Once the X seconds delay is complete, it will sound an alarm (burp in this case) that the monitoring is complete. The acceleration monitoring can be restarted by pressing the A button that is also on board the Circuit Playground Bluefruit.

##### Non-blocking timer
CircuitPython operates on a single thread meaning it can only do 1 action at a time. Doing multiple things has to be done one after the other, but in order to be able to do "multiple things at once", one solution is to wait for something to happen (an event) to trigger another action (a callback). Python and CircuitPython have a `time` module `sleep` function that delays execution of the next task by some number of seconds. While it's delaying execution, nothing can happen during this time. All execution is stopped. This is called a blocking timer.

But if you want to be able to do multiple things "at once", you need a way to not block execution of other tasks that need to happen. A non-blocking timer implementation allows you to keep track of multiple events that need to happen, when they need to happen and what to do when their time is up.

The solution to this problem is in `timer_collection.py` and tests in `test_timer_collection.py`. This module was written using TDD, where the tests were written first, then the code. A mock was used for Python's `time` module to simulate time elapsing and the current time. A Makefile was also created for ease of use in running the tests. Tests can be run by running `make run_tests`.

The timer collection is a class. When initialized, it holds an empty list of `Timer` objects. It also records the `last_ticks` as the current time from `time.monotonic()`. A one-shot or periodic timer can be started in this collection and a callback function to be executed when the timer expires included, and it'll be added to the list of timers. Once a timer is created, you need to run the timer collection in order for time to pass. The timer collection's `run` method returns the time until the next timer is due to expire. Thus you can do this in the `while True:` (main execution) loop:

```
while True:
    time_until_next = timer_collection.run()

    if time_until_next != None:
        time.sleep(time_until_next)
    else:
        time.sleep(1)
```

If there is time until the next timer is due to expire, then we'll sleep that amount of time. There is nothing to do until that next timer is ready to expire. If there are no more timers due to expire, then it'll just sleep for 1 second (this is dependent on system requirements and what other features your application is running).

Inside the timer collection's `run` method, it figures out which timer is due to expire next by checking the remaining time (ticks) for all of the timers in the list. If there is no remaining time left for a timer, it will also run the callback function that was passed in when the timer was added.

This non-blocking timer collection allows multiple timers to be created and execute their callbacks at different times without blocking (i.e. waiting and stopping for it) the execution of another timer. This allows for more complex hardware applications with multiple timers and events.

##### Acceleration monitor with alarm application
The non-blocking timer implementation is used in an application where the acceleration can be monitored on the top of a washing machine, and once the change in acceleration slows down, it'll sound an alarm to let you know that the cycle is complete.

The code is `accelerometer_alarm.py`. It initializes a heartbeat LED (to let you know that the board's application code is running) and the periodic timer that monitors the acceleration. Every time the periodic timer's callback is called, it compares the previous acceleration in x, y, and z with the current acceleration in x, y, and z, calculates the difference, and if the absolute value of the difference between these two acceleration vectors is less than some threshold (set to 0.5 m/s^2), then the debounce count is incremented. The difference must be debounced X times (set to 5) before the cycle is deemed complete. This ensures that the acceleration value is consistent with no large spikes. Once the debounce time has completed, then a delay timer is started (a one-shot timer for X seconds, set to 5), then the alarm will sound (in this case a burp sound) indicating that the cycle is complete.

##### Other examples
Other example uses of the non-blocking timer can be found in the `/examples` folder. `blinker.py` blinks the Neopixel LEDs on the Bluefruit at various rates. `pedometer.py` is a rudimentary (and not at all accurate) pedometer step counter that monitors the acceleration and once it matches a certain pattern, records a step taken.
