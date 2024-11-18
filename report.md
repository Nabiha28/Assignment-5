# Quicksort Algorithm: Design, Implementation, and Analysis

1. Introduction

The aim is to implement and analyze the Quicksort algorithm in both deterministic and randomized ver- sions. Quicksort is one of the most popular and efficient sorting algorithms in practice that follows divide-and-conquer paradigm. Its average-case time complexity equals O(n log n), while, in the case of poor choice of the pivot, the worst-case time complexity may be as bad as O(n²). The work discusses the trade-offs between determinism and randomness of the algorithm, followed by empirical tests to ascertain their performance.


 2. Design Choices

2.1. Choice of Pivot Selection

This fact makes the method of selecting the pivot a critical factor in the performance of the Quicksort algorithm. Here are some design choices for the two versions of Quicksort in this project:

-Deterministic Quicksort: In this version, the pivot will be chosen as the middle element of the array.This choice was made because selecting the middle element is simple to implement and generally performs reasonably well in practice, though it can degrade to O(n²) in some cases, especially with already sorted or reverse-sorted data.

- Randomized Quicksort: In the randomized version, the pivot is chosen randomly from the array. Randomization helps mitigate the risk of consistently encountering the worst-case scenario, which occurs when the pivot is always the smallest or largest element. By randomizing the pivot, we expect the algorithm to behave more reliably, with an average-case time complexity of O(n log n) for all kinds of input data distributions.

2.2. Recursive Implementation

Both the deterministic and randomized versions of Quicksort use a recursive implementation. Quicksort works by selecting a pivot element, partitioning the array into two subarrays  and recursively sorting these subarrays. The recursion is the core feature of the divide-and-conquer approach.

Base Case: If the subarray has zero or one entry, that would be the recursion's base case. The subarray is already sorted by definition, therefore nothing needs to be done.
Recursive Case: In this scenario, divide the array after selecting a pivot. Quicksort should be run recursively on the two subarrays.


2.3. Partitioning Strategy

For both versions of Quicksort, the partitioning strategy is the same:

 After choosing the pivot, the array is partitioned, with all members larger than the pivot going to the right and all elements less than the pivot going to the left. After that, the pivot element is positioned in its ultimate sorted location. 

 3. Implementation Details

3.1. Deterministic Quicksort Implementation

The deterministic version of Quicksort is implemented by selecting the pivot as the middle element of the array. The algorithm works as follows:

1.Base Case: If the array has 0 or 1 element, return it as it is already sorted.
2. Partitioning: Split the array into three parts based on the pivot:
   - Elements less than the pivot.
   - Elements equal to the pivot (useful for handling duplicates).
   - Elements greater than the pivot.
3. Recursive Sorting: Recursively apply Quicksort to the left and right subarrays.

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [y for y in arr if y < pivot]
    middle = [y for y in arr if y == pivot]
    right = [y for y in arr if y > pivot]
    return quicksort(left) + middle + quicksort(right)

3.2. Randomized Quicksort Implementation

In the randomized version, the pivot is selected randomly using Python's `random.randint()` function. This random selection aims to reduce the chances of encountering the worst-case performance that may occur in the deterministic version when the pivot selection is poor.

The implementation is almost identical to the deterministic version, except that the pivot selection is randomized.


import random

def randomized_quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]
    left = [y for y in arr if y < pivot]
    middle = [y for y in arr if y == pivot]
    right = [y for y in arr if y > pivot]
    return randomized_quicksort(left) + middle + randomized_quicksort(right)


 4. Time and Space Complexity Analysis

 4.1. Time Complexity

Best and Average Case:
- The average-case time complexity of Quicksort is O(n log n) for both deterministic and randomized variants. At each level of recursion, this happens when the pivot splits the array into two almost equal subarrays.

- In the best-case scenario, the pivot splits the array into two equal halves, leading to an optimal balance of recursion. Each recursive call reduces the problem size by approximately half, resulting in a logarithmic number of recursive levels, and linear time complexity for partitioning at each level.

Worst Case:
- The worst-case time complexity for the deterministic version of Quicksort is O(n²). This happens when the pivot is always chosen poorly (e.g., the smallest or largest element), causing the array to be partitioned in an unbalanced way, leading to O(n) recursive levels and O(n) work at each level.
- The randomized version of Quicksort mitigates the risk of encountering the worst-case by selecting a random pivot, resulting in an expected worst-case time complexity of O(n log n). While the worst-case can still technically happen, it is highly unlikely, making this version more stable.

4.2. Space Complexity

- Both the deterministic and randomized versions of Quicksort have O(log n) space complexity. This is due to the recursion stack, which can go as deep as the logarithm of the array's length in the best and average cases.
- In the worst case, if the array is always split into one very large subarray and one very small subarray, the recursion stack could go as deep as O(n), but this is rare in practice, especially with the randomized version.

5. Empirical Results

5.1. Performance Comparison

The runtime performance of the randomized and deterministic Quicksort variants on various input sizes was empirically compared. Randomly generated arrays containing 100, 1000, and 10,000 elements were used for the testing. 


 5.2. Conclusion from Empirical Testing
- The randomized Quicksort performs better on average due to its ability to avoid the worst-case scenario. 
- The deterministic Quicksort can degrade to O(n²) time complexity, especially with poorly ordered data, whereas the randomized version generally maintains O(n log n) time complexity.
