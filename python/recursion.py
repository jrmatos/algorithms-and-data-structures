def regressive(i):
    print(i)
    if i <= 1:
        return
    else:
        regressive(i-1)

def fat(x):
    if x == 1:
        return x
    else:
        return x * fat(x - 1)

# 0 1 1 2 3 5 8 13
def fibonacci(n, f):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def sum_divide_to_conquer(l):
    l_size = len(l)
    middle = l_size / 2

    if l_size > 1:
        return sum_divide_to_conquer(l[:middle]) + sum_divide_to_conquer(l[middle:])

    if l_size == 1:
        return l[0]
    
    return 0


# regressive(20)
# print(fat(5))
# print(fibonacci(4))
print(sum_divide_to_conquer([100,25, 25,30]))

