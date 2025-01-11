""" 

You are given an array 'arr' sorted in non-decreasing order and a number 'x'. You must return the index of the lower bound of 'x'.


Note:

1. For a sorted array 'arr', 'lower_bound' of a number 'x' is defined as the smallest index 'idx' such that the value 'arr[idx]' is not less than 'x'.If all numbers are smaller than 'x', then 'n' should be the 'lower_bound' of 'x', where 'n' is the size of array.

2. Try to do this in O(log(n)).


Example:

Input: 'arr' = [1, 2, 2, 3] and 'x' = 0

Output: 0

Explanation: Index '0' is the smallest index such that 'arr[0]' is not less than 'x'.


"""

""" 
Key Concept: The largest element in the array that is less than or equal to the target.
"""

from typing import List
import bisect

def lower_bound(arr: List[int], target: int)-> int:
    """ 
    pythonic way to compute lower bound: 
    
    return bisect.bisect_left(arr, target)
    """
    n = len(arr)
    lb = n
    low = 0
    high = n-1
    while low<=high:
        mid = (low+high)//2
        if arr[mid]>=target:
            # search to left as much as possible!!
            lb = mid # track the current index
            high = mid-1
        else:
            low = mid+1
    return lb
            


if __name__=='__main__':
    arr = [1, 2, 2, 3]
    x = 2
    
    print(lower_bound(arr, x))  