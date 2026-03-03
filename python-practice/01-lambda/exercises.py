'''
Exercise 1 — basic lambda:
'''
# Regular function
def square(x):
    return x * x

# Same as lambda
square_lambda = lambda x: x * x

print(square(5))
print(square_lambda(5))