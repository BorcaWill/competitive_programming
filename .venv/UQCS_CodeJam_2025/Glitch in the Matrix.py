#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'count_glitchy_rows' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n1
#  2. INTEGER m1
#  3. 2D_INTEGER_ARRAY mat
#

def count_glitchy_rows(n1, m1, mat):
    # Write your code here
    messed_up = 0
    for i in range(n1):
        if sum(mat[i]) == m1:
            messed_up += 1
    return messed_up
            



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().rstrip().split())))

    result = count_glitchy_rows(n, m, matrix)

    fptr.write(str(result) + '\n')

    fptr.close()
