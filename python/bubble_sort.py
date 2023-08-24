from data import average, best, worst

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr

print(bubble_sort(best))
print(bubble_sort(average))
print(bubble_sort(worst))
