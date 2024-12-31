""" 
You are given an array 'a' of size 'n' and an integer 'k'.


Find the length of the longest subarray of 'a' whose sum is equal to 'k'.


Example :

Input: ‘n’ = 7 ‘k’ = 3
‘a’ = [1, 2, 3, 1, 1, 1, 1]

Output: 3

Explanation: Subarrays whose sum = ‘3’ are:

[1, 2], [3], [1, 1, 1] and [1, 1, 1]

Here, the length of the longest subarray is 3, which is our final answer.


"""
""" 
        Naive Solution: 
        
        res = 0
            for i in range(len(arr)):
                sum = 0
                for j in range(i, len(arr)):
                    sum += arr[j]
                    if sum == k:
                        res = max(res, j-i+1)
            return res 
"""

from typing import List

def longestSubarrayWithSumK(arr: List[int], k:int)->int:
    # i,j =0, 0
    # res = 0
    # sum = 0
    # while(j<len(arr)):
    #     sum += arr[j]
    #     if(sum<k):
    #         j+=1
    #     elif(sum==k):
    #         res = max(res, j-i+1)
    #         sum -= arr[i]
    #         i+=1
    #         j+=1
    # return res
    ...
        
        

if __name__=='__main__':
    arr = [1, 2, 3, 1, 1, 1, 1]
    k = 3
    print(longestSubarrayWithSumK(arr, k))    