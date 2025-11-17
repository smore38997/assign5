import sys
sys.setrecursionlimit(20000)

import random, time
import matplotlib.pyplot as plt

# Deterministic quicksort
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quicksort_det(arr, low, high):
    while low < high:
        p = partition(arr, low, high)
        # Tail recursion optimization: recurse on smaller partition
        if p - low < high - p:
            quicksort_det(arr, low, p - 1)
            low = p + 1
        else:
            quicksort_det(arr, p + 1, high)
            high = p - 1

# Randomized quicksort
def randomized_partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    return partition(arr, low, high)

def quicksort_rand(arr, low, high):
    while low < high:
        p = randomized_partition(arr, low, high)
        if p - low < high - p:
            quicksort_rand(arr, low, p - 1)
            low = p + 1
        else:
            quicksort_rand(arr, p + 1, high)
            high = p - 1

# Benchmark
def benchmark(sort_func, data):
    arr = data.copy()
    start = time.time()
    sort_func(arr, 0, len(arr)-1)
    return time.time() - start

sizes = [500, 1000, 2000, 4000, 8000]
distributions = ["random", "sorted", "reverse"]

results_det = {d: [] for d in distributions}
results_rand = {d: [] for d in distributions}

for n in sizes:
    data_random = [random.randint(0, n) for _ in range(n)]
    data_sorted = list(range(n))
    data_reverse = list(range(n, 0, -1))
    sets = {"random": data_random, "sorted": data_sorted, "reverse": data_reverse}

    for dist in distributions:
        results_det[dist].append(benchmark(quicksort_det, sets[dist]))
        results_rand[dist].append(benchmark(quicksort_rand, sets[dist]))

# Plots
for dist in distributions:
    plt.figure()
    plt.plot(sizes, results_det[dist], label="Deterministic")
    plt.plot(sizes, results_rand[dist], label="Randomized")
    plt.xlabel("Input Size")
    plt.ylabel("Time (seconds)")
    plt.title(f"Quicksort Comparison - {dist} input")
    plt.legend()
    plt.tight_layout()
    plt.show()
