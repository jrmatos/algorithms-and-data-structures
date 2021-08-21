from data import average, best, worst
# For sorted, nearly sorted or reversed sorted cases quicksort takes n^2 comparions
# For average cases it takes nlogn comparisons

# average case O(nlogn)
# worst case O(n^2)

def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        smallers_than_pivot = [i for i in arr[1:] if i <= pivot]
        biggers_than_pivot = [i for i in arr[1:] if i > pivot]

        return quick_sort(smallers_than_pivot) + [pivot] + quick_sort(biggers_than_pivot)

print(quick_sort(average)) # average case: 11 recursions
print(quick_sort(worst)) # wrost case: 17 recursions
print(quick_sort(best)) # best case: 17 recursions
