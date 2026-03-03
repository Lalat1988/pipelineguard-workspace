'''
In this example, we define a decorator function `my_decorator` that takes another function `func` as an argument. 
The `wrapper` function is defined inside the decorator and is responsible for adding additional behavior before and after the execution of the original function.
'''

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function runs")
        result = func(*args, **kwargs)
        print("After function runs")
        return result
    return wrapper

@my_decorator
def say_something(msg):
    print(f"Message: {msg}")
    
print("Calling decorated function:")
say_something("Hello")