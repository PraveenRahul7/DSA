""" 
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".


Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings. 
"""
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
            Sorting the list of strings:

            After sorting, the string with the smallest prefix similarity appears at the start (strs[0]) and the one with the largest difference appears at the end (strs[-1]).

            This is because the sorting is lexicographical, so differences are maximized at the boundaries.

            Comparing only the first and last elements:

            Since these are the most different in terms of prefix, finding the common prefix between them is sufficient.

            Any prefix that matches between the first and last element will match with all the middle elements.

            Prefix comparison:

            You loop through the characters of both the first and last elements.

            As soon as characters do not match, you break out of the loop.

            If they match, you keep appending to the result string res.
        """
        strs.sort()
        res = ""
        min_len = min(len(strs[0]), len(strs[-1]))
        for i in range(min_len):
            if strs[0][i]==strs[-1][i]:
                res+=strs[0][i]
            else:
                break
        return res     