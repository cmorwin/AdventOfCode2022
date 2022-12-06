# We're going to time our script for fun
import time

_timer_time = 0


# Start the timer
def start_timer():
    _timer_time = time.process_time()


# Stop the timer and print the time it took
def stop_timer():
    time_taken = time.process_time() - _timer_time
    print(f"  Calculation took {(time_taken)*1000:.4} milliseconds")


# Read in the file contents
def read_input(fn="input.txt"):
    try:
        with open(fn, "r") as f:
            return f.read()
    except FileNotFoundError:
        print("File not found")
        exit
