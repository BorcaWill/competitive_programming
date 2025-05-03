#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'mostUniqueDish' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts 2D_STRING_ARRAY logs as parameter.
#

def mostUniqueDish(logs):
    # Write your code here
    dict_of_dishes = {}
    for log in logs:
        if log[0] not in dict_of_dishes:
            dict_of_dishes[log[0]] = [log[1]]
        else:
            if log[1] not in dict_of_dishes[log[0]]:
                dict_of_dishes[log[0]].append(log[1])
    max_unique = 0
    max_name = ""
    for dish, ingredients in dict_of_dishes.items():
        candidate = len(ingredients)
        if candidate > max_unique:
            max_unique = candidate
            max_name = dish
    return [max_name, str(max_unique)]



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    log_data = []

    for _ in range(n):
        log_data.append(input().rstrip().split())

    result = mostUniqueDish(log_data)

    fptr.write(' '.join(result))
    fptr.write('\n')

    fptr.close()
