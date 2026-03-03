'''
Wrapper Arguments Fixed - Modify the wrapper function in your decorator to accept any number of positional and keyword arguments using *args and **kwargs. This allows the decorator to work with functions that have different signatures without causing errors.
Demonstrate the modified decorator by applying it to a function that takes arguments and showing that it works correctly without any issues.
'''

def my_decorator(func):
    def wrapper(*args, **kwargs):       # accepts anything
        print("before")
        result = func(*args, **kwargs)  # passes everything through
        print("after")
        return result
    return wrapper

@my_decorator
def greet(name):
    print(f"Hello {name}")

greet("Lalat")              # works now