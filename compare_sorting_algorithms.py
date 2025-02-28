import random
import timeit

from insertion_sort import insertion_sort
from merge_sort import merge_sort

def generate_random_list(size):
    return [random.randint(0, 100000) for _ in range(size)]

def compare_sorting_algorithms():
    sizes = [1000, 5000, 10000, 50000]

    for size in sizes:
        print(f"=== List size: {size} ===")

        data = generate_random_list(size)

        data_for_insertion = data[:]
        data_for_merge = data[:]
        data_for_timsort = data[:]

        insertion_time = timeit.timeit(
            lambda: insertion_sort(data_for_insertion), number=1
            )
        print(f"Insertion sort: {insertion_time:.6f} seconds")

        merge_time = timeit.timeit(
            lambda: merge_sort(data_for_merge), number=1
            )
        print(f"Merge sort: {merge_time:.6f} seconds")

        timsort_time = timeit.timeit(
            lambda: sorted(data_for_timsort), number=1
            )
        print(f"Timsort: {timsort_time:.6f} seconds")

if __name__ == "__main__":
    compare_sorting_algorithms()