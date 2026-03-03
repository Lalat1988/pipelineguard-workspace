'''
Practical Timing Decorator - Create a decorator called timer that measures the execution time of a function. The decorator should print the time taken to execute the function in seconds. 
Use the time module to measure the start and end time of the function execution. 
Apply this decorator to a sample function that simulates a slow operation (e.g., using time.sleep) and 
demonstrate the output showing the execution time.
'''

import time
import functools

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "done"

print("Calling decorated function:")
slow_function()