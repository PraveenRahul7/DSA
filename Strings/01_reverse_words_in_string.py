""" 
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.


Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.




"""

class Solution:
    @staticmethod
    def reverseWords(s):
        """_summary_
        
        | Method       | Time Complexity | Space Complexity        | In-Place |
        | ------------ | --------------- | ----------------------- | -------- |
        | `reverse()`  | **O(n)**        | **O(1)**                | ✅        |
        | `reversed()` | **O(n)**        | **O(n)** (if converted) | ❌        |
        | `join()`     | **O(n)**        | **O(n)**                | ❌        |
        | `split()`    | **O(n)**        | **O(n)**                | ❌        |
        
        split(separator=None, maxsplit=-1) -> list

            Splits a string into a list of substrings based on a specified separator.
            If no separator is provided, it splits on any whitespace. 
            `maxsplit` defines the maximum number of splits.

            Time Complexity: O(n), where n is the length of the string.
            Space Complexity: O(n) for storing the substrings.
            
        join(iterable) -> str

            Concatenates the elements of an iterable (like list or tuple) into a single string, 
            with the string calling `join()` acting as the separator.

            Time Complexity: O(n), where n is the total length of all strings combined.
            Space Complexity: O(n) for creating the new string.
        
        """
        return "".join(s.split().reverse())



if __name__=='__main__':
    s = input()
    client = Solution.reverseWord(s)
    
