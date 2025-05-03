#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'highest_unique' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY picks as parameter.
#

def highest_unique(picks):
    # Write your code here
    dict = {}
    for i in picks:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    candidate = []
    for i, appearances in dict.items():
        if appearances == 1:
            candidate.append(i)
    if len(candidate) == 0:
        return -1
    return max(candidate)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ratings = list(map(int, input().rstrip().split()))

    result = highest_unique(ratings)

    fptr.write(str(result) + '\n')

    fptr.close()
