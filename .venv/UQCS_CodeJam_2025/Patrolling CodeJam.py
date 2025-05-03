#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'patrol' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY seating as parameter.
#

def patrol(i, j, seating):
    # Write your code here
    table_count = 0
    for k in range(i):
        if sum(seating[k]) == 0:
            continue
        for l in range(j):
            if seating[k][l]:
                table_count += 1
                seating = chain_reaction(seating, i, j, k, l)
    return table_count
def chain_reaction(seating,i, j, k, l):
    seating[k][l] = 0
    if k+1 < i and seating[k+1][l]:
        seating = chain_reaction(seating,i, j, k+1, l)
    if l+1 < j and seating[k][l+1]:
        seating = chain_reaction(seating,i, j, k, l+1)
    return seating

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    m = int(input().strip())

    seating = []

    for _ in range(n):
        seating.append(list(map(int, input().rstrip().split())))

    result = patrol(seating)

    fptr.write(str(result) + '\n')

    fptr.close()
