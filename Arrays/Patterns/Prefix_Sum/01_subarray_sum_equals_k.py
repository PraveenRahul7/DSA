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

"""
Prefix Sum Intution:
Core Idea: 
    The prefix sum technique is a powerful way to solve problems related to subarrays and their sums. The main idea is to maintain a cumulative sum of elements as we iterate through the array, allowing us to quickly calculate the sum of any subarray.
Intuition:
    1. The prefix sum array is constructed such that each element at index i in the prefix sum array represents the sum of all elements from the start of the original array up to index i.
    2. To find the sum of a subarray from index i to j, we can use the prefix sum array: 
        - If i > 0, then sum(i, j) = prefix_sum[j] - prefix_sum[i-1]
        - If i == 0, then sum(i, j) = prefix_sum[j]
    3. This allows us to compute the sum of any subarray in constant time O(1) after an initial O(n) preprocessing step to create the prefix sum array.
"""
""" 
Approach: 

    1. Initialize a variable prefix_sum to 0, which will keep track of the cumulative sum of elements as we iterate through the array.
    2. Create a dictionary prefix_count to store the frequency of each prefix sum encountered. Initialize it with {0: 1} to handle cases where a subarray starting from the beginning equals k.
    3. Initialize a variable count to 0, which will store the total number of subarrays whose sum equals k.
    4. Iterate through each element num in the array nums:
        a. Add the current element num to prefix_sum.
        b. Check if (prefix_sum - k) exists in prefix_count. If it does, add its frequency to count. This means that there are prefix_count[prefix_sum - k] subarrays ending at the current index that sum to k.
        c. Update the frequency of prefix_sum in prefix_count. If prefix_sum is already present, increment its count; otherwise, initialize it to 1.
    5. Finally, return the count of subarrays whose sum equals k.

"""
from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        prefix_count = {0: 1} # prefix_sum keeps track of the cumulative sum of all elements from the beginning up to the current position.
        """ 
        The initialization prefix_count = {0: 1} is crucial.

            This means "we've seen a prefix sum of 0 exactly once" before starting our loop
            It handles the case where a complete subarray from the beginning sums to exactly k
            Without it, we would miss subarrays that start from the beginning of the array
        """
        count = 0

        for num in nums:
            """ 
            For each element, we:
                Add it to our running prefix sum
                Check if (prefix_sum - k) exists in our dictionary. If it does, that means there's a subarray that sums to k
                Update our dictionary with the current prefix sum
            """
            prefix_sum += num

            if (prefix_sum - k) in prefix_count:
                count += prefix_count[prefix_sum - k]

            prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1

        return count
            