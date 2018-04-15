#!/bin/python3

import os
import sys

#
# Complete the diagonalDifference function below.
#
def diagonalDifference(a):
    #
    # Write your code here.
    #
    sum1 = 0
    sum2 = 0
    for i in range(0, a.__len__()):
        sum1 += a[i][i]

    i = 0
    j = a.__len__() - 1
    while i < a.__len__():
        sum2 += a[i][j]
        i += 1
        j -= 1

    print abs(sum1-sum2)

# if __name__ == '__main__':
#     f = open(os.environ['OUTPUT_PATH'], 'w')

n = int(input())

a = []

for _ in range(n):
    a.append(list(map(int, input().rstrip().split())))

diagonalDifference(a)
    # result = diagonalDifference(a)
    #
    # f.write(str(result) + '\n')
    #
    # f.close()
