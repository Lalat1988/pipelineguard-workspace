'''
# functools.wraps is a decorator that helps to preserve the original function's 
# metadata (like name, docstring, etc.) when you create a wrapper function (decorator).
'''


def my_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def compare_tables():
    """Compares source and target tables"""
    pass

print(compare_tables.__name__)  # what do you see?
print(compare_tables.__doc__)   # what do you see?