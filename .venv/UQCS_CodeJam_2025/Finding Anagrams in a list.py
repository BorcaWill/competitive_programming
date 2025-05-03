#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'solution' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER counts
#  2. STRING_ARRAY words
#

def solution(counts, words):
    # Write your code here
    anagram_list = []
    words_sets_list = []
    words_list = []
    count = 0
    for word in words:
        word = word.lower()
        candidate = set(word)
        if word not in words_list:# is a different word
            words_list.append(word)#register a different word
            if candidate not in words_sets_list:#is a new set of alphas
                words_sets_list.append(candidate)#register a new set of alphas
            else:#is an anagram set
                anagram_list.append(candidate)
    words_list = []
    for word in words:
        word = word.lower()
        candidate = set(word)
        if word not in words_list:# is a different word
            if candidate in anagram_list:#is an anagram
                count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    size = int(input().strip())

    arr = input().rstrip().split()

    answer = solution(size, arr)

    fptr.write(str(answer) + '\n')

    fptr.close()
