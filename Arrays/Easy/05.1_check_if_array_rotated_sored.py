""" 
Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.

There may be duplicates in the original array.

Note: An array A rotated by x positions results in an array B of the same length such that B[i] == A[(i+x) % A.length] for every valid index i.

 

Example 1:

Input: nums = [3,4,5,1,2]
Output: true
Explanation: [1,2,3,4,5] is the original sorted array.
You can rotate the array by x = 3 positions to begin on the element of value 3: [3,4,5,1,2].
Example 2:

Input: nums = [2,1,3,4]
Output: false
Explanation: There is no sorted array once rotated that can make nums.
Example 3:

Input: nums = [1,2,3]
Output: true
Explanation: [1,2,3] is the original sorted array.
You can rotate the array by x = 0 positions (i.e. no rotation) to make nums
"""
""" 
Approach:
    1. Initialize a variable count to 0.
    2. Iterate through the array nums using a for loop.
    3. For each element nums[i], check if it is greater than the next element nums[(i+1)%n]. This is done using the modulo operator to wrap around to the start of the array. The main concept is to check if the current element is greater than the next element in a circular manner, if there are more than 1 such instances, then the array is not sorted.
    4. If it is, increment the count by 1.
    5. If count exceeds 1, return False.
    6. If the loop completes without exceeding count, return True.
"""


from typing import List
class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        count = 0
        for i in range(n):
            if nums[i]>nums[(i+1)%n]:
                count+=1
            if count>1:
                return False
        return True
        