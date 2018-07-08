def longest_common_substring(str1, str2):
    table = [[0 for j in range(len(str2))] for i in range(len(str1))]

    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                if i - 1 >= 0 and j - 1 >= 0:
                    table[i][j] = table[i - 1][j - 1] + 1
                else:
                    table[i][j] = 1

    (max_i, max_j) = (0, 0)
    for i in range(len(str1)):
        for j in range(len(str2)):
            if table[i][j] > table[max_i][max_j]:
                (max_i, max_j) = (i, j)

    return table[max_i][max_j]


print(longest_common_substring("cricket", "wicket"))
print(longest_common_substring("ale", "hale"))
print(longest_common_substring("healthy", "wealthy"))
print(longest_common_substring("in", "kin"))
print(longest_common_substring("blue", "clues"))
