#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'min_bulk_rotation' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER N
#  2. INTEGER E
#  3. INTEGER_ARRAY angles
#  4. INTEGER_ARRAY powers
#

def min_bulk_rotation(N, E, angles, powers):
    # Write your code here

    if E > sum(powers):
        return -1
    dict = {}
    for i in range(N):
        if angles[i] not in dict.keys():
            dict[angles[i]] = powers[i]
        else:
            dict[angles[i]] += powers[i]
    keys = sorted(dict.keys())
    out_put_powers = 0
    for key in keys:
        out_put_powers += dict[key]
        if out_put_powers >= E:
            return key
    return -1



    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # read the scalars

    first_multiple_input = input().rstrip().split()

    N = int(first_multiple_input[0])

    E = int(first_multiple_input[1])

    angles = list(map(int, input().rstrip().split()))

    powers = list(map(int, input().rstrip().split()))

    answer = min_bulk_rotation(N, E, angles, powers)

    fptr.write(str(answer) + '\n')

    fptr.close()
