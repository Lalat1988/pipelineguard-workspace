'''
Exercise 6 — lambda with map and filter:'''
numbers = [1, 2, 3, 4, 5]

# map transforms every element
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)  # [2, 4, 6, 8, 10]

# filter selects elements where condition is True
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4]