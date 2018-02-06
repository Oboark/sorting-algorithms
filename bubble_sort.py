import numpy as np 
import random

def bubble_sort(a):
    """Bubble sort algorithm O(n^2)"""
    n = len(a)-1
    # perform sort until array is fully sorted
    for _ in range(n,0,-1):
        # iterate over every value in the array
        for i in range(n):
            # if n[i] is more than n[i+1], swap them
            if a[i] > a[i+1]:
                temp = a[i]
                a[i] = a[i+1]
                a[i+1] = temp
    return a
    
a = list(range(1000))
random.shuffle(a)

print("Unsorted list: ", a)
print("Sorted List: ", bubble_sort(a))