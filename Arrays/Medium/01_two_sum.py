""" 
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

"""

from typing import List

def two_sum(arr: List[int], target: int)->List[int]:
    """
    use hashing. 
    hash table stores element as key and index as value (mp[arr[i]] = i)
    
    If target-arr[i] is present return result!!!
    """
    lookup = {}
    for i in range(len(arr)):
        complement = target-arr[i]
        if complement in lookup:
            return [lookup[complement], i]
        lookup[arr[i]] = i
    return []


if __name__=='__main__':
    arr = [2,7,11,15]
    target = 9
    print(two_sum(arr, target))    