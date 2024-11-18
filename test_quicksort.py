# test_quicksort.py

from quicksort import quicksort, randomized_quicksort

def test_quicksort():
    assert quicksort([3, 6, 8, 10, 1, 2, 1]) == [1, 1, 2, 3, 6, 8, 10]
    assert quicksort([3, 3, 3, 3, 3]) == [3, 3, 3, 3, 3]
    assert quicksort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    print("Deterministic Quicksort tests passed!")

def test_randomized_quicksort():
    assert randomized_quicksort([3, 6, 8, 10, 1, 2, 1]) == [1, 1, 2, 3, 6, 8, 10]
    assert randomized_quicksort([3, 3, 3, 3, 3]) == [3, 3, 3, 3, 3]
    assert randomized_quicksort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    print("Randomized Quicksort tests passed!")

if __name__ == "__main__":
    test_quicksort()
    test_randomized_quicksort()
