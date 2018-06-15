def find_smallest(arr):
    smallest_index = 0
    smallest_value = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < smallest_value:
            smallest_value = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr):
    new_arr = []
    while len(arr) != 0:
        smallest_index = find_smallest(arr)
        new_arr.append(arr[smallest_index])
        arr.pop(smallest_index)
    return new_arr


print(selection_sort([3, 2, 5]))
print(selection_sort([3, 2, 5, 4, 0]))
