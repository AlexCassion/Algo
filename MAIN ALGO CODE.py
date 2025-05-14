import time

comparison_count = 0
comparison_list = []  # To track the list of comparisons

def partition(arr, low, high):
    global comparison_count, comparison_list
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        comparison_count += 1
        comparison_list.append((arr[j], pivot))  # Track comparison
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

# Input
arr = list(map(int, input("Enter numbers (Standard Quick Sort): ").strip().split()))
comparison_count = 0
comparison_list = []

# Track the time taken by the QuickSort process using perf_counter
start_time = time.perf_counter()

# Call the quicksort function
quicksort(arr, 0, len(arr) - 1)

end_time = time.perf_counter()

# Output
print("\nSorted array (Standard Quick Sort):", arr)
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
