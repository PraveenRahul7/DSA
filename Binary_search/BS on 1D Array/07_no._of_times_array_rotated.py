""" 
You have been given a sorted array/list 'arr' consisting of ‘n’ elements. You are also given an integer ‘k’.

Now the array is rotated at some pivot point unknown to you.

For example, if 'arr' = [ 1, 3, 5, 7, 8], then after rotating 'arr' at index 3, the array will be 'arr' = [7, 8, 1, 3, 5].


Now, your task is to find the index at which ‘k’ is present in 'arr'.


Note :

1. If ‘k’ is not present in 'arr', then print -1.
2. There are no duplicate elements present in 'arr'. 
3. 'arr' can be rotated only in the right direction.

Example:

Input: 'arr' = [12, 15, 18, 2, 4] , 'k' = 2

Output: 3

Explanation:
If 'arr' = [12, 15, 18, 2, 4] and 'k' = 2, then the position at which 'k' is present in the array is 3 (0-indexed).

"""
from typing import List
class Solution:
    def search(self, arr: List[int], target: int) -> int:
        """ 
        Identify which half is sorted. Either left or right. 
        Use the sorted property!!!. Given target attack the sorted part first and check if target is within the sorted half and eleminate accordingly.
        """
        n = len(arr)
        low, high = 0, n-1

        while low<=high:
            mid = low + (high-low)//2
            if arr[mid] == target:
                return mid
            if arr[low]<=arr[mid]:
                if arr[low]<=target and target<=arr[mid]:
                    high = mid-1
                else:
                    low = mid+1
            else:
                if arr[mid]<=target and target<=arr[high]:
                    low = mid+1
                else:
                    high = mid-1
        return -1
