'''

'''

import time

def fetch_data(name):
    print(f"Fetching {name}...")
    time.sleep(2)  # simulates slow DB or API call
    print(f"Done fetching {name}")
    return f"data from {name}"

start = time.time()
fetch_data("table_A")
fetch_data("table_B")
fetch_data("table_C")
print(f"Total time: {time.time() - start:.2f}s")
# Takes 6 seconds — runs one by one