""" 
You are given an array 'arr' of length 'n', consisting of integers.


A subarray is a contiguous segment of an array. In other words, a subarray can be formed by removing 0 or more integers from the beginning and 0 or more integers from the end of an array.


Find the sum of the subarray (including empty subarray) having maximum sum among all subarrays.


The sum of an empty subarray is 0.


Example :

Input: 'arr' = [1, 2, 7, -4, 3, 2, -10, 9, 1]

Output: 11

Explanation: The subarray yielding the maximum sum is [1, 2, 7, -4, 3, 2].



"""

from sys import *

def maxSubarraySum(arr, n) :
    """ 
    Logic: 
        We have the result computed till ai-1. so work b/w ai-1 and ai. ai-1+ai is one subarray and ai is other possibility. So compare b/w ai-1+ai and ai and compute max. 
    """
    max_sum = arr[0]
    res = arr[0]
    for i in range(1, n):
        max_sum = max(max_sum+arr[i], arr[i])
        res = max(max_sum, res)
    return res 


def KadaneAlgo(arr, n):
    maxi = -maxsize-1 # maximum sum
    sum = 0

    for i in range(n):
        sum += arr[i]

        maxi = max(maxi, sum)

        # If sum < 0: discard the sum calculated.
        # discarding subarrays with a negative cumulative sum because continuing with such subarrays cannot possibly lead to a larger maximum sum for any future subarray.
        if sum < 0:
            sum = 0

    # To consider the sum of the empty subarray
    # uncomment the following check:

    #if maxi < 0: maxi = 0

    return maxi


def printmaxSubarraySum(arr, n):
    
    maxi = -maxsize-1 # maximum sum
    sum = 0
    start = -1
    
    ans_start, ans_end = -1, -1
    for i in range(n):
        if sum==0: start = i
        sum += arr[i]

        if sum>maxi:
            maxi = sum
            ans_start = start
            ans_end = i

        # If sum < 0: discard the sum calculated.
        # discarding subarrays with a negative cumulative sum because continuing with such subarrays cannot possibly lead to a larger maximum sum for any future subarray.
        if sum < 0:
            sum = 0
    # Print the maximum sum subarray
    if ans_start != -1 and ans_end != -1:  # Valid indices found
        print("Maximum Subarray Sum:", maxi)
        print("Subarray:", end=" ")
        for i in range(ans_start, ans_end + 1):
            print(arr[i], end=" ")
        print()
    else:
        print("No subarray with positive sum found.")

if __name__=='__main__':
    arr = [-1, -2]
    print(maxSubarraySum(arr, len(arr)))  
    print(KadaneAlgo(arr, len(arr)))
    print(printmaxSubarraySum(arr, len(arr)))