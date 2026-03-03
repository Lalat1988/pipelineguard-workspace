'''
Exercise 5 — PipelineGuard flavored:
'''

# Simulating filtering validation results
validation_results = [
    {"table": "orders", "mismatches": 5},
    {"table": "customers", "mismatches": 0},
    {"table": "products", "mismatches": 12},
    {"table": "inventory", "mismatches": 0}
]

# Filter only tables with mismatches
failed = list(filter(lambda r: r["mismatches"] > 0, validation_results))

# Sort by mismatch count descending
sorted_failed = sorted(failed, key=lambda r: r["mismatches"], reverse=True)

print("Failed tables:", sorted_failed)