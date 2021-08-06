# 1) 두 문자가 같을 때, 좌측위에 있는 숫자에 1을 더한 값

# 2) 두 문자가 다를 때, 좌측이나 위에 있는 숫자중 큰 값, 동일한 값일 때는 위의 값

#     x A C A Y K P
#   y 0 0 0 0 0 0 0
#   C 0 0 1 1 1 1 1
#   A 0 1 1 2 2 2 2
#   P 0 1 1 2 2 2 3
#   C 0 1 2 2 2 2 3
#   A 0 1 2 3 3 3 3
#   K 0 1 2 3 3 4 4

import sys

str1 = input()
str2 = input()

len1 = len(str1)
len2 = len(str2)

lcs = [[0 for i in range(len2 + 1)] for j in range(len1 + 1)]

for i in range(1, len(str1) + 1):
    for j in range(1, len(str2) + 1):
        if str1[i-1] == str2[j-1]:
            lcs[i][j] = lcs[i-1][j-1] + 1
        else:
            lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])

print(lcs[-1][-1])