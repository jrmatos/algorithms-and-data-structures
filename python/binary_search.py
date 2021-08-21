# O(log n)

def binary_search(items, item):
    bottom = 0
    top = len(items) - 1

    while bottom <= top:
        middle = int((bottom + top) / 2)

        guess = items[middle]

        if guess == item:
            return middle
        
        if guess > item:
            top = middle - 1
        else:
            bottom = middle + 1
    
    return None


items = [1,29,30,40,57,72,100]

print(binary_search(items, 30))
print(binary_search(items, 404))
