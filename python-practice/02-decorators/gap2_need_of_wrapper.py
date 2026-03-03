'''
Need for Wrapper Function in Decorators - Explain why a wrapper function is necessary in a decorator.
Discuss how the wrapper function allows us to add functionality before and after the execution of the original function, and how it helps in maintaining the original function's signature and return value. 
Provide an example of a simple decorator that uses a wrapper function to log the execution of a function, and demonstrate how the wrapper function is essential for this purpose.
'''


def my_decorator(func):
    def wrapper():          # no args here
        print("before")
        result = func()     # no args passed
        print("after")
        return result
    return wrapper

@my_decorator
def greet(name):            # but this function needs an argument
    print(f"Hello {name}")

greet("Lalat")              # this will crash because wrapper doesn't accept any arguments, but greet does. We need to modify the wrapper to accept *args and **kwargs to handle this case.