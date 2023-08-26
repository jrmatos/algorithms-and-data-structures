def is_sorted(arr):
    if len(arr) < 2:
        return True

    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            return False

    return True