'''
In this example, we define a simple decorator `my_decorator` that wraps a function 
and adds behavior before and after the function runs. 
We then apply this decorator manually to the `say_something` function and call 
the decorated version to see the added behavior in action.
'''

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function runs")
        result = func(*args, **kwargs)
        print("After function runs")
        return result
    return wrapper

def say_something(msg):
    print(f"Message: {msg}")

# Apply decorator manually
decorated = my_decorator(say_something)
print("Calling decorated function:")
decorated("Hello")