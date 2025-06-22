""" 
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 3:

Input: nums = [1,2,3]
Output: 3

"""

""" 
Intuition:
To solve the problem of robbing houses arranged in a circle, we can break it down into two cases:
1. Rob houses from the first house to the second last house (excluding the last house).
2. Rob houses from the second house to the last house (excluding the first house).

"""

from functools import lru_cache
from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        """ 
        IBH Method:
        1. Induction: We need to find the maximum amount of money we can rob from a circular arrangement of houses.
        2. Base Condition: If there are no houses, return 0. If there is one house, return the amount in that house.
        3. Hypothesis: Assume we can find the maximum amount for the first i houses.
        4. Induction Step: For each house, we can either rob it (and add its value to the maximum amount from the previous non-adjacent house) or skip it (and take the maximum amount from the previous house).
        Time Complexity: O(n) - Linear time complexity due to the single pass through the list  
        Space Complexity: O(n) - Space used by the recursion stack.
        5. Edge Cases: If the input list is empty, return 0.
        6. Handle the circular nature of the houses by considering two cases:
        - Rob houses from the first house to the second last house (excluding the last house).
        - Rob houses from the second house to the last house (excluding the first house).
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        @lru_cache(maxsize=None)
        def solve(i, end):
            if i>end:
                return 0
            include = nums[i]+solve(i+2, end)
            exclude = solve(i+1, end)
            return max(include, exclude)
        handle_first_element = solve(0, n-2)
        handle_second_element = solve(1, n-1)
        return max(handle_first_element, handle_second_element)