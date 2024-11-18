# Assignment-5
# Quicksort Algorithm: Implementation, Analysis, and Randomization

 Overview

This assignment provides both deterministic and randomized implementations of the Quicksort algorithm. In addition to theoretical time complexity analysis of Quicksort, it also compares the running times empirically of the two versions for different input sizes.

The key objectives include:
- Implementing Quicksort in its deterministic form (using a fixed pivot).
- Implementing a randomized version of Quicksort (randomly selecting the pivot).
- Analyzing the time complexity of both versions, including their best, average, and worst-case scenarios.
- Running empirical tests to compare the performance of the deterministic and randomized versions for different input sizes.

 Files

- `quicksort.py`: Both the deterministic and randomized implementations of Quicksort are in here.
- `test_quicksort.py`: contains unit tests to check the correctness of the two Quicksort versions.
- `performance_analysis.py`: this script runs empirical performance tests. It compares the execution time of both Quicksort versions.
- `report.md`: Report with findings of the empirical tests, comparison of the performances and discussion of time and space complexities.
- `README.md`: This file represents an overview of the project and how to run the code.

How to Run the Code

Steps to run the code and analyze the performance of both versions of Quicksort:

 1. Clone the repository

Clone this repository to local machine:

git clone https://github.com/Nabiha28/Assignment-5.git
cd Assignment-5

2. Run the Unit Tests
The unit tests will check the correctness of both the deterministic and randomized Quicksort algorithms. To run the tests, execute the following command:
python test_quicksort.py

3. Run the Performance Analysis
To perform the empirical tests comparing the execution time of the deterministic and randomized versions of Quicksort, run:
python performance_analysis.py

4. Review the Performance Analysis
The detailed findings from the empirical tests are included in the analysis.md file. The performance comparison between the randomized and deterministic Quicksorts is compiled in this report along with information on how randomization impacts runtime.

Summary of Findings
Time Complexity:
Best and Average Case: Both deterministic and randomized Quicksort have a time complexity of O(n log n) in the best and average cases.
Worst Case: The worst-case time complexity for the deterministic version is O(n²), which occurs when the pivot is poorly chosen (e.g., always the first or last element). The randomized version avoids this by randomly selecting the pivot, making the worst-case time complexity O(n log n) on average.
Space Complexity:
Both implementations of Quicksort have the space complexity of O(log n), since each call has a size proportional to the logarithm of the size of the input.
Empirical Results:
The analysis of the running times provided evidence that Quicksort's randomized version actually outperforms its deterministic counterpart, especially when applied to fairly large files. This is because it avoids, for those cases where an optimal choice of pivot is not guaranteed, the worst-case scenario that might arise for the deterministic version.

Conclusion:
The randomized version of Quicksort is more robust, and it tends to outperform the deterministic version as the size of the input increases. The randomized pivot selection reduces the likelihood of encountering the worst-case time complexity, making it a preferable choice for most practical use cases.

