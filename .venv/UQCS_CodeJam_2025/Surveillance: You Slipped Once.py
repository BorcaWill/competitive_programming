#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'max_streak_with_one_slip' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def max_streak_with_one_slip(arr):
    # Write your code here
    if sum(arr) == 0:
        return 0
    elif sum(arr) == 1:
        return len(arr)
    max_streak = 0
    left = 0
    one_count = 0

    for right in range(len(arr)):
        if arr[right] == 1:
            one_count += 1
        # start a streak
        while one_count > 1:
            if arr[left] == 1:
                one_count -= 1
            left += 1
        max_streak = max(max_streak, right - left + 1)  

    return max_streak

    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    input_array = list(map(int, input().rstrip().split()))

    result = max_streak_with_one_slip(input_array)

    fptr.write(str(result) + '\n')

    fptr.close()
