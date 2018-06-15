def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        if item == list[mid]:
            return mid
        elif item > list[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return None


print(binary_search([1,2,3,4], 3))
print(binary_search([1,2,3,4], 5))
print(binary_search([1,2,3,4], 2))
print(binary_search([1,2,3,4], 1))
