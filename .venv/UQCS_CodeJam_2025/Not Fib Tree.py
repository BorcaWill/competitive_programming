#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countFibonacciNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER count
#  2. INTEGER_ARRAY nums
#

def countFibonacciNumbers(count, nums):
    # Write your code here
    result = 0
    for i in range(count):
        if nums[i] in fiboArray(100):    
            result += 1
    return result

def fiboArray(n):
    memo = (n+1) * [-1]
    for i in range(n+1):
        memo[i] = fibRecursion(i,memo)
    return memo

def fibRecursion(n,memo):
    if n == 0 or n == 1:
        return n
    if memo[n] != -1:
        return memo[n]
    memo[n] = fibRecursion(n - 1,memo) + fibRecursion(n - 2,memo)
    return memo[n]

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    list_of_numbers = list(map(int, input().rstrip().split()))

    result = countFibonacciNumbers(n, list_of_numbers)

    fptr.write(str(result) + '\n')

    fptr.close()
