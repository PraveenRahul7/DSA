""" 
 Problem statement

You have been given a sorted array/list of integers 'arr' of size 'n' and an integer 'x'.


Find the total number of occurrences of 'x' in the array/list.


Example:

Input: 'n' = 7, 'x' = 3
'arr' = [1, 1, 1, 2, 2, 3, 3]

Output: 2

Explanation: Total occurrences of '3' in the array 'arr' is 2.

"""

""" 
Pythonic Way: 


import bisect
def count(arr: [int], n: int, x: int) -> int:
    # Your code goes here
    first_occur = -1
    last_occur = n

    first_occur = bisect.bisect_left(arr,x)
    last_occur = bisect.bisect_right(arr, x)-1
    
    return last_occur-first_occur+1
    
    
"""
from typing import *
def count(nums: List[int], n: int, target: int) -> int:
    first_occur, last_occur = -1, -1
    low, high = 0, n - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] >= target:
            high = mid - 1
        else:
            low = mid + 1
        
        if nums[mid] == target:
            first_occur = mid

        
    low, high = 0, n - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] <= target:
            low = mid + 1
        else:
            high = mid - 1
            
      
        if nums[mid] == target:
            last_occur = mid

    if first_occur == -1:
        return 0
    return last_occur-first_occur+1