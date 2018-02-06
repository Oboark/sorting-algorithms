import numpy as np 
import random 

def insertion_sort(a):
    """Insertion sort algorithm O(n^2)"""
    n = len(a)
    # iterate over values
    for i in range(1, n):
        # our current value
        x = a[i]
        # the index value we will compare our current value to, which is to the left
        j = i - 1
        # because j is going lower and lower we don't want to perform this when j is a negative number
        # and if the value that we will compare (j) is higher than our current value
        while j >= 0 and a[j] > x:
            # if so, shift the value to the right
            a[j+1] = a[j]
            # shift the value to the left to the comparison value
            j = j - 1
        a[j+1] = x

    return a

a = list(range(100000))
random.shuffle(a)

print("Unsorted list: ", a)
print("Sorted List: ", insertion_sort(a))