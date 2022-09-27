import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    test=len(arr)
    j=test-2
    value=arr[test-1]
    while j>=0 and value<arr[j]:
        arr[j+1]=arr[j]
        j-=1
        b=' '.join([str(elem) for elem in arr])
        print(b)

    arr[j+1]=value
    b=' '.join([str(elem) for elem in arr])
    print(b)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)


