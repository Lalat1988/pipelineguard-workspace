'''
Args and Kwargs - Create a function called show_arguments that accepts any number of positional arguments 
(*args) and keyword arguments (**kwargs). The function should print the received arguments in a readable format.
Demonstrate the function by calling it with various combinations of positional and keyword arguments.'''

def show_arguments(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

show_arguments(1, 2, 3)
show_arguments(name="Lalat", role="engineer")
show_arguments(1, 2, name="Lalat")