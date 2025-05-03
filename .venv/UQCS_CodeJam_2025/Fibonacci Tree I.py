#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'fibonacciLeaves' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER num as parameter.
#

def fibonacciLeaves(num):
    # Write your code here
    memo = (num+1) * [-1]
    return fibRecursion(num,memo)
def fibRecursion(n,memo):
    if n == 0 or n == 1:
        return 1
    if memo[n] != -1:
        return memo[n]
    memo[n] = fibRecursion(n - 1,memo) + fibRecursion(n - 2,memo)
    return memo[n]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Reading the input integer n

    n = int(input().strip())

    # Defining function to calculate leaf nodes in Fibonacci Tree

    # Start writing your logic

    # Write your code here

    # Invoking the fibonacciLeaves function with parameter n

    result = fibonacciLeaves(n)

    # Printing the result

    fptr.write(str(result) + '\n')

    fptr.close()
