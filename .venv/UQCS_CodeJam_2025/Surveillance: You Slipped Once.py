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
    restored_i = 0
    i = 0
    slipped = 0
    while i < len(arr):
        if arr[i] == 0:# start a streak
            streak = 1
            slliped = 0
            i += 1
            while i < len(arr) and slliped < 3:
                if arr[i] == 0:
                    streak += 1
                    i += 1
                elif slipped == 0:
                    slipped += arr[i]
                    streak += 1
                    i += 1
                else:
                    break
                if slipped < 2 or arr[i] == 0:
                    streak += 1
                i += 1
                if slipped == 1:
                    restored_i = i
                    slipped = 2
            if slipped >= 2:
                i = restored_i
            slipped = 0
            max_streak = max(max_streak, streak)
        else:
            i += 1
    return max_streak

    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    input_array = list(map(int, input().rstrip().split()))

    result = max_streak_with_one_slip(input_array)

    fptr.write(str(result) + '\n')

    fptr.close()
