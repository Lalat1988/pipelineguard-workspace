'''
In Python, functions are first-class objects, which means they can be treated 
like any other object. They can be assigned to variables, 
passed as arguments to other functions, and returned from other functions. 
This allows for a lot of flexibility in how we can use and manipulate 
functions in our code.
'''

def greet(name):
    return f"Hello {name}"

# Functions can be assigned to variables
say_hello = greet
print(say_hello("Lalat"))

# Functions can be passed as arguments
def run_function(func, value):
    return func(value)

print(run_function(greet, "Lalat"))