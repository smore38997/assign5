def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1  # pointer for smaller elements

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # Place pivot in correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quicksort(arr, low, high):
    """
    Sorts the array arr[low:high+1] in place using Quicksort.
    """
    if low < high:
        # Partition step: arr[p] is now at correct position
        p = partition(arr, low, high)

        # Recursively sort elements before and after partition
        quicksort(arr, low, p - 1)
        quicksort(arr, p + 1, high)


# Example usage:
if __name__ == "__main__":
    data = [10, 7, 8, 9, 1, 5]
    print("Original array:", data)

    quicksort(data, 0, len(data) - 1)
    print("Sorted array:", data)
