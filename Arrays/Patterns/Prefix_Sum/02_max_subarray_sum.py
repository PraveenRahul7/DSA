""" 
Given an integer array nums, find the subarray with the largest sum, and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
 

"""

"""
Max Subarray Sum using Prefix Sum (Kadane's Algorithm) 
The prefix sum approach for max subarray sum is often implemented as Kadane's algorithm:
"""
def max_subarray_sum(nums):

    """ 
    This is a dynamic programming approach where at each element, we decide whether to:

        Start a new subarray from the current element (if previous sum is negative)
        Continue the existing subarray by adding the current element
    """
    current_sum = 0
    max_sum = float('-inf')
    
    for num in nums:
        # Either start a new subarray or continue the previous one
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum