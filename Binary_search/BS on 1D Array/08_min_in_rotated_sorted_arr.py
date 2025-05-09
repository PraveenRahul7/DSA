""" 
You are given an array 'arr' of size 'n' having unique elements that has been sorted in ascending order and rotated between 1 and 'n' times which is unknown.


The rotation involves shifting every element to the right, with the last element moving to the first position. For example, if 'arr' = [1, 2, 3, 4] was rotated one time, it would become [4, 1, 2, 3].


Your task is to find the minimum number in this array.


Note :

All the elements in the array are distinct. 


Example :

Input: arr = [3,4,5,1,2]

"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        low, high = 0, n-1
        res = float('inf')-1
        while low<=high:
            mid = low+(high-low)//2
            if nums[low]== nums[mid] and nums[mid] == nums[high]:
                #if there are duplicates. 
                res = min(res, nums[low])
                low +=1
                high -=1
                continue
            if nums[low]<=nums[mid]:
                res = min(res, nums[low])
                low = mid+1
            else:
                res = min(res, nums[mid])
                high = mid-1
        return res
        