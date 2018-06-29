def merge_list(l1, l2):
    soln = []
    for s1 in l1:
        for s2 in l2:
            if set(s1).isdisjoint(set(s2)):
                soln.append(s1 + s2)
    return soln


def add_solutions(sol1, sol2):
    for v in sol2:
        present = False
        for a in sol1:
            if set(a) == set(v):
                present = True
                break
        if not present:
            sol1.append(v)


def sub(arr, val):
    if val == 0:
        return [[]]
    arr.sort()
    solutions = {k: [[k]] for k in arr}
    i = 0
    while i < len(arr):
        first_key = arr[i]
        first_key_soln = solutions[first_key]
        for j in range(i + 1, len(arr)):
            next_key = arr[j]
            new_key = first_key + next_key
            if new_key > val:
                break
            new_solutions = merge_list(first_key_soln, solutions[next_key])
            if (len(new_solutions)) > 0:
                if new_key not in solutions:
                    solutions[new_key] = []
                add_solutions(solutions[new_key], new_solutions)
        i += 1
        arr = list(solutions.keys())
        arr.sort()
    if val in solutions:
        return solutions[val]
    else:
        return []


print(sub([10, 3, 7, 8, 15, 12], 20))
print(sub([10, 3, 7, 8, 15, 12], 1000))
print(sub([10, 3, 7, 8, 15, 12], 22))
print(sub([10, 12, 5, 6, 8, 3, 2], 20))
