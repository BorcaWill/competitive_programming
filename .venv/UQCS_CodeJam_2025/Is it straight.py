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
    if [0,0] in pts:
        pts.remove([0,0])
        count -= 1
    ratio = (pts[0][0]-pts[1][0]+10**4+1)/(pts[0][1]-pts[1][1]+10**4+1)

    for i in range(1,count-1):
        if (pts[i][0]-pts[0][0]+10**4+1)/(pts[i][1]-pts[0][1]+10**4+1) != ratio:
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
