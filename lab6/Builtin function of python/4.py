import time
import math

def delayed_sqrt(number, delay):
    time.sleep(delay / 1000)
    return math.sqrt(number)

num = 25100
delay = 2123
print(f"Square root of {num} after {delay} milliseconds is {delayed_sqrt(num, delay)}")
