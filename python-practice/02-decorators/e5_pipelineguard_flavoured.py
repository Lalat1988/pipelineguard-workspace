'''
PipelineGuard Flavoured Decorator - Create a decorator called log_validation that logs the start and end of a data validation function. 
The decorator should print the name of the function being validated, the time taken for validation, 
and the result of the validation (e.g., "PASS" or "FAIL").
Use the time module to measure the execution time of the validation function.
Apply this decorator to a sample validation function that compares two 
datasets (e.g., comparing row counts of source and target tables) and returns a validation result. 
Demonstrate the output showing the logs for the validation process. 
'''

import functools
import time

def log_validation(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Starting validation: {func.__name__}")
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"[LOG] Completed in {elapsed:.4f}s — Result: {result}")
        return result
    return wrapper

@log_validation
def compare_tables(source_count, target_count):
    print(f"Comparing source count ({source_count}) with target count ({target_count})")
    mismatches = abs(source_count - target_count)
    return {"mismatches": mismatches, "status": "PASS" if mismatches == 0 else "FAIL"}

compare_tables(1000, 995)
compare_tables(500, 500)