from data import average, best, worst

# TODO: make it a real bubblesort
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[j] > arr[i]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr

print(bubble_sort(worst))