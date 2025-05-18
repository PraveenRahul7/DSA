"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
 

Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107

"""
from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        # Initialize prefix_count with {0: 1} to handle cases where a subarray starting from the beginning equals k.
        prefix_count = {0: 1} 
        count = 0

        for num in nums:
            prefix_sum += num
            
            if (prefix_sum - k) in prefix_count:
                count += prefix_count[prefix_sum - k]

            if prefix_sum in prefix_count:
                prefix_count[prefix_sum] += 1
            else:
                prefix_count[prefix_sum] = 1

        return count
            