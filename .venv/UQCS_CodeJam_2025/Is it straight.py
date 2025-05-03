#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'checkStraightLine' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER count
#  2. 2D_INTEGER_ARRAY pts
#

def checkStraightLine(count, pts):
    # Write your code here
    x = pts[0][0]
    y = pts[0][1]
    for i in range(1,count-1):
        if (pts[i][0]-x)*(pts[i+1][1]-y) != (pts[i+1][0]-x)*(pts[i][1]-y):
            return "false"
    return "true"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    coords = []

    for _ in range(n):
        coords.append(list(map(int, input().rstrip().split())))

    result = checkStraightLine(n, coords)

    fptr.write(result + '\n')

    fptr.close()
