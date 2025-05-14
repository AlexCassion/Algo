import time
import random

comparison_count = 0

def insertion_sort(arr, low, high):
    """Insertion Sort for small subarrays."""
    for i in range(low + 1, high + 1):
        key = arr[i]
        j = i - 1
        while j >= low and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def randomized_partition(arr, low, high):
    """Randomized Partition to avoid worst-case pivot selection."""
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    return partition(arr, low, high)

def partition(arr, low, high):
    """3-Way Partitioning to handle duplicates efficiently."""
    global comparison_count
    pivot = arr[high]
    i = low - 1
    j = low
    while j < high:
        comparison_count += 1
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
        elif arr[j] > pivot:
            j += 1
        else:
            # If arr[j] == pivot, just skip it
            j += 1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort(arr, low, high):
    """Refining QuickSort algorithm."""
    if low < high:
        if high - low < 10:  # Switch to Insertion Sort for small subarrays
            insertion_sort(arr, low, high)
        else:
            # Use Randomized Pivot Selection
            pi = randomized_partition(arr, low, high)
            quicksort(arr, low, pi - 1)
            quicksort(arr, pi + 1, high)

# Input
arr = list(map(int, input("Enter numbers (Refining Quick Sort): ").strip().split()))
comparison_count = 0

# Track the time taken by the QuickSort process using perf_counter
start_time = time.perf_counter()

# Call the quicksort function
quicksort(arr, 0, len(arr) - 1)

end_time = time.perf_counter()

# Output
print("\nSorted array (Refining Quick Sort):", arr)
print("Total comparisons:", comparison_count)

# Time complexity estimation based on comparisons
n = len(arr)
if comparison_count < n * (n - 1) / 2:
    time_complexity = "Best Case (O(n log n))"
else:
    time_complexity = "Worst Case (O(n^2))"

print("\nTime complexity estimation based on comparisons:", time_complexity)

# Print the time taken by the algorithm
print("\nTime taken to sort the array: {:.6f} seconds".format(end_time - start_time))
