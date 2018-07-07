def longest_common_subsequence(str1, str2):
    table = [[0 for j in range(len(str2))] for i in range(len(str1))]

    for i in range(len(str1)):
        for j in range(len(str2)):
            top = 0 if i - 1 < 0 else table[i - 1][j]
            left = 0 if j - 1 < 0 else table[i][j - 1]
            diagonal = 0 if j - 1 < 0 or i - 1 < 0 else table[i - 1][j - 1]
            if str1[i] == str2[j]:
                table[i][j] = diagonal + 1
            else:
                table[i][j] = max(top, left)

    return table[-1][-1]


print(longest_common_subsequence("docker", "dollar"))
print(longest_common_subsequence("fish", "fosh"))
print(longest_common_subsequence("fort", "fosh"))
print(longest_common_subsequence("cricket", "ticket"))
print(longest_common_subsequence("brute", "writ"))
