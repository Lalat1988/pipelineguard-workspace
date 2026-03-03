'''
In the previous example, we saw that the wrapper function's name and docstring were not preserved. To fix this, we can use the `functools.wraps` decorator from the `functools` module. This decorator copies the metadata from the original function to the wrapper function.
'''

import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def compare_tables():
    """Compares source and target tables"""
    pass

print(compare_tables.__name__)  # now shows compare_tables
print(compare_tables.__doc__)   # now shows the docstring