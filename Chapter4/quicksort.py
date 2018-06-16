def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x <= pivot]
        right = [x for x in arr[1:] if x > pivot]
        return quicksort(left) + [pivot] + quicksort(right)


print(quicksort([1,2,3]))
print(quicksort([9,8,7,6]))
print(quicksort([4,5,4,6,3]))
