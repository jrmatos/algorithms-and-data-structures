import math
from typing import List
from data import load_integers_from_file
from sort_utils import is_sorted

# O(nlogn)
def qsorti(arr: List[int]):
    if len(arr) < 2: # base case
        return arr
    else: # recursive case
        pivot_index = math.floor(len(arr) / 2)
        pivot = arr[pivot_index]
        lte_pivot = []
        gt_pivot = []

        for i in range(len(arr)):
            if i == pivot_index:
                continue # ignore pivot index
            if arr[i] <= pivot:
                lte_pivot.append(arr[i])
            else:
                gt_pivot.append(arr[i])

        return qsorti(lte_pivot) + [pivot] + qsorti(gt_pivot)

if __name__ == "__main__":
    input = load_integers_from_file("input.txt")
    sorted = qsorti(input)

    assert len(input) == len(sorted)
    assert is_sorted(sorted)

    # print(is_sorted(input))
    # print(is_sorted(sorted))
