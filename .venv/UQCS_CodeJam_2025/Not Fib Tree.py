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
        if isFibonacci(nums[i]):
            result += 1
    return result

def isFibonacci(num):
    # Check if num is a Fibonacci number
    if num in [1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,4181,6765,10946]:
        return True
    elif num> 10946:
        i = 20
        while True:
            if fibonacciLeaves(i) == num:
                return True
            elif fibonacciLeaves(i) < num:
                i += 1
            else:
                return False

    
def fibonacciLeaves(num):
    # Write your code here
    if num == 0 or num == 1:
        return 1
    elif num == 5:
        return 8
    elif num == 10:
        return 89
    elif num == 20:
        return 10946
    elif num > 1:
        return fibonacciLeaves(num - 1) + fibonacciLeaves(num - 2)
    else: 
        raise ValueError("Input must be a non-negative integer")
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    list_of_numbers = list(map(int, input().rstrip().split()))

    result = countFibonacciNumbers(n, list_of_numbers)

    fptr.write(str(result) + '\n')

    fptr.close()
