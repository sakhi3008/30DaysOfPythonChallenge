#Challenge - Create a decorator to log function execution time

import time
def log_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time:.4f} seconds")
        return result
    return wrapper

@log_execution_time
def process_large_dataset():
    total = 0
    for i in range(1, 10**6):
        total += i**0.5
    print("Finished processing dataset.")
 

process_large_dataset()

