""" 

Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.


"""

from typing import List

def max_consecutive_ones(arr:List[int])->int:
    res = 0
    count = 0
    for i in range(0, len(arr)):
        if arr[i] == 0:
            count = 0
        else: 
            count +=1
        res = max(count, res)
    return res
        
            
        
    

if __name__=='__main__':
    arr = [1,1,0,1,1,1]
    print(max_consecutive_ones(arr))    