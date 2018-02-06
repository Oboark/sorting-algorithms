import numpy as np 
import random

def selection_sort(a):
    """Selection sort algorithm O(n^2)"""
    n = len(a)
    # iterate over list
    for i in range(n):
        # assume smallest value is the current value
        iMin = i
        # check for smaller values after the current smallest values
        for j in range(i+1, n):
            # if current value is smaller than current smallest value, assign smallest value to that
            if a[j] < a[iMin]:
                iMin = j

        # if the smallest value is not equal to the current value, swap them
        if iMin != i:
            temp = a[i] 
            a[i] = a[iMin]
            a[iMin] = temp
    return a

a = list(range(1000))
random.shuffle(a)

print("Unsorted list: ", a)
print("Sorted List: ", selection_sort(a))