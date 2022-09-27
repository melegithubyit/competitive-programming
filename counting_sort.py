import math
import os
import random
import re
import sys


# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.

def countingSort(arr):
    frequency = [0 for _ in range(100)]
    min_num = 0
    max_num = 99
    range_of_num = 100
    for i in range(len(arr)):
        frequency[arr[i]] += 1
    return frequency


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
