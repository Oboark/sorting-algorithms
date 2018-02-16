import numpy as np 
import random 

def merge(left, right):
    """Merges and sorts both lists"""
    result = []
    left_idx, right_idx = 0, 0
    
    # while we haven't exhausted one of the lists yet (left, right)
    while left_idx < len(left) and right_idx < len(right):
        # append the smallest element to result, and move to the next element
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1

    # if one of the lists still has elements (true), append all the other elements to result
    if left:
        result.extend(left[left_idx:])
    if right:
        result.extend(right[right_idx:])

    return result

def merge_sort(a):
    """Merge sort algorithm O(n log n)"""
    # return if the list only has one element
    if len(a) <= 1:
        return a

    # cut the list in half and store the according halves
    mid = len(a) // 2
    left = a[:mid]
    right = a[mid:]

    # recursively sort until everything is sorted
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

a = list(range(1000))
random.shuffle(a)

print("Unsorted list: ", a)
print("Sorted List: ", merge_sort(a))
