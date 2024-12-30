""" 
Problem Statement: Given an array, we have to find the largest element in the array.

Example:

Input: 'n' = 5, 'arr' = [1, 2, 3, 4, 5]

Output: 5

Explanation: From the array {1, 2, 3, 4, 5}, the largest element is 5.
 
"""
from typing import List

def get_largest(arr: List[int])->int:
    
    if not arr:
        return
    largest = arr[0]
    for num in arr[1:]:
        if num>largest:
            largest = num
    return largest
    
if __name__=='__main__':
    try:
        arr = list(map(int, input().split()))
        print(get_largest(arr))
    except ValueError as e:
        print(f"Error: {e}")