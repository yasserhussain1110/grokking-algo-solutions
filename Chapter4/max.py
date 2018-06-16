def maximum(arr):
    if len(arr) == 0:
        return None
    elif len(arr) == 1:
        return arr[0]
    else:
        return max(arr[0], maximum(arr[1:]))


print(maximum([1,2,7,3]))
