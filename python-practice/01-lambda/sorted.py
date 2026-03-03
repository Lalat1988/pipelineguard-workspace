'''
Exercise 4 — lambda with sorted:
'''

employees = [
    {"name": "Alice", "salary": 90000},
    {"name": "Bob", "salary": 75000},
    {"name": "Charlie", "salary": 110000}
]
sorted_employees = sorted(employees, key=lambda e: e["salary"])
print(sorted_employees)


