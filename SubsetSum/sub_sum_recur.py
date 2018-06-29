def sub(arr, val):
    if val == 0:
        return [[]]
    elif len(arr) == 0 and val != 0:
        return []
    res = []
    for i in range(len(arr)):
        partial_solutions = sub(arr[i + 1:], val - arr[i])
        current_solution = [[arr[i]] + x for x in partial_solutions]
        res += current_solution
    return res


print(sub([10, 3, 7, 8, 15, 12], 20))
print(sub([10, 3, 7, 8, 15, 12], 1000))
print(sub([10, 3, 7, 8, 15, 12], 22))
print(sub([10, 12, 5, 6, 8, 3, 2], 20))
