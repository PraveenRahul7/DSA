""" 
A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.
"""


"""  
Because the straightforward linear scan solution isn't using all of the clues given in the question. These clues, including

   -> No adjacent two numbers are the same
   -> the two end of the arrays are -∞
   -> You can return any peak.

"""

from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Handle edge cases for small input sizes
        if n == 1:  # Single element is always a peak
            return 0
        if nums[0] > nums[1]:  # Peak at the start
            return 0
        if nums[n - 1] > nums[n - 2]:  # Peak at the end
            return n - 1

        # Binary search for peak in the range [1, n-2]
        left, right = 1, n - 2
        while left <= right:
            mid = left + (right - left) // 2
            
            # Check if the current element is a peak
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            
            #If increasing flow before mid => sorted, then mid is current high. Then search on right side.
            if nums[mid-1]<nums[mid]:
                left = mid+1
            else:  #if decreasing flow on right side of mid=> then currently mid is the peak, search for left side.
                right = mid-1
        
        # Default return value (though it should not reach here in a valid input)
        return -1

