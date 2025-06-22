""" 
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
"""

""" 
Intution: 
Pick the current house and add the maximum amount from the previous non-adjacent house, or skip the current house and take the maximum amount from the previous house.
"""
from functools import lru_cache
from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        """ 
        IBH Method:
        1. Induction: We need to find the maximum amount of money we can rob without alerting the police.
        2. Base Condition: If there are no houses, return 0. If there is one house, return the amount in that house.
        3. Hypothesis: Assume we can find the maximum amount for the first i houses
        4. Induction Step: For each house, we can either rob it (and add its value to the maximum amount from the previous non-adjacent house) or skip it (and take the maximum amount from the previous house).
        Time Complexity: O(n) - Linear time complexity due to the single pass through the list
        Space Complexity: O(n) - Space used by the recursion stack.
        5. Edge Cases: If the input list is empty, return 0.
        """
        n = len(nums)
        @lru_cache(maxsize=None)
        def solve(i):
            if i >= n:
                return 0
            include = nums[i] + solve(i+2)
            not_include = solve(i+1)
            return max(include, not_include)
        return solve(0)