# O(n^2)

def findMin(arr):
    min_value = arr[0]
    min_index = 0

    for i in range(1, len(arr)):
        if arr[i] < min_value:
            min_value = arr[i]
            min_index = i
    
    return min_index

def selectionSort(arr):
    newArr = []

    for i in range(len(arr)):
        menor = findMin(arr)
        newArr.append(arr.pop(menor))

    return newArr

items = [100,123,512,7,1,10,2]

print("before: {}".format(items))
print("after: {}".format(selectionSort(items)))
