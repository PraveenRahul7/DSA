""" 
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:

Input: nums = [], target = 0
Output: [-1,-1]


"""

""" 
Pythonic Way: 

import bisect
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        fp = bisect.bisect_left(nums, target)
        lp = bisect.bisect_right(nums, target) -1

        if fp<len(nums) and nums[fp]==target and lp>=0 and nums[lp]==target:
            return [fp, lp]
        return [-1, -1]
        

"""

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        n = len(nums)
        first_occur, last_occur = -1, -1

        # Find first occurrence of target
        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] >= target:
                high = mid - 1
            else:
                low = mid + 1
            
            # Update first_occur only if nums[mid] == target
            if nums[mid] == target:
                first_occur = mid

        # Find last occurrence of target
        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] <= target:
                low = mid + 1
            else:
                high = mid - 1
            
            # Update last_occur only if nums[mid] == target
            if nums[mid] == target:
                last_occur = mid

        return [first_occur, last_occur]