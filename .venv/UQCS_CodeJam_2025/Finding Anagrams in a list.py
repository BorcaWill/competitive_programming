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
    anagram_map = {}
    anagram_count = {}
    count = 0

    for word in words:
        word = word.lower()
        sorted_word = "".join(sorted(word))
        if sorted_word in anagram_map:
            anagram_map[sorted_word].add(word)
            anagram_count[sorted_word] += 1
        else:
            anagram_map[sorted_word] = {word}
            anagram_count[sorted_word] = 1

    for word, value in anagram_map.items():
        if len(value) > 1:
            count += anagram_count[word]
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    size = int(input().strip())

    arr = input().rstrip().split()

    answer = solution(size, arr)

    fptr.write(str(answer) + '\n')

    fptr.close()
