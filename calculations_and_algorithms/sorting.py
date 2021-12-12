from random import randrange
import numpy as np

unsorted_array = np.asarray([randrange(100) for _ in range(50)])
print(f"Before sorting array:\n{unsorted_array}")

def bubble_sort(numbers):
    swapped = True
    while swapped:
        swapped = False
        for idx in range(len(numbers) - 1):
            if numbers[idx] < numbers[idx + 1]:
                numbers[idx], numbers[idx + 1] = numbers[idx + 1], numbers[idx]
                swapped = True

library_sorted_array = sorted(unsorted_array, reverse=True)
print(f"After sorting array by standard library: {library_sorted_array}")

bubble_sort(unsorted_array)

print(f"After sorting array: {unsorted_array}")

print(f"Checking if the arrays sorted by these two ways is the same : {(unsorted_array == library_sorted_array).all()}")

