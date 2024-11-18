# performance_analysis.py
import random
import time
from quicksort import quicksort, randomized_quicksort

def measure_time(algorithm, arr):
    """Measure the time taken for the algorithm to sort the array."""
    start_time = time.time()
    algorithm(arr)
    return time.time() - start_time

def run_performance_tests():
    sizes = [100, 1000, 10000]
    for size in sizes:
        arr = [random.randint(0, 1000) for _ in range(size)]
        deterministic_time = measure_time(quicksort, arr)
        randomized_time = measure_time(randomized_quicksort, arr)
        print(f"Size {size}: Deterministic: {deterministic_time:.5f}s, Randomized: {randomized_time:.5f}s")

if __name__ == "__main__":
    run_performance_tests()
