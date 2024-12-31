""" 
You have been given an array a of n non-negative integers.You have to check whether the given array is sorted in the non-decreasing order or not.


Your task is to return 1 if the given array is sorted. Else, return 0.


Example :

Input: n = 5, a = [1, 2, 3, 4, 5]
Output: 1

The given array is sorted in non-decreasing order; hence the answer will be 1.




"""
from typing import List

def is_sorted(arr: List[int])->bool:
    
    # return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            return 0
    return 1
         
    
                    
if __name__=='__main__':
    try:
        arr = list(map(int, input().split()))
        print(is_sorted(arr))
    except ValueError as e:
        print(f"Error: {e}")