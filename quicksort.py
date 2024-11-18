# quicksort.py
import random

def quicksort(arr):
    """Deterministic Quicksort."""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def randomized_quicksort(arr):
    """Randomized Quicksort."""
    if len(arr) <= 1:
        return arr
    pivot_index = random.randint(0, len(arr) - 1)  
    pivot = arr[pivot_index]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quicksort(left) + middle + randomized_quicksort(right)
