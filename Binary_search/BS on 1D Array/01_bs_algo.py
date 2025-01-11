""" 

You are given an integer array 'A' of size 'N', sorted in non-decreasing order. You are also given an integer 'target'. Your task is to write a function to search for 'target' in the array 'A'. If it exists, return its index in 0-based indexing. If 'target' is not present in the array 'A', return -1.


Note:

You must write an algorithm whose time complexity is O(LogN)


"""

from typing import List

def search(arr: List[int], target: int)-> int:
    
    """ 
    Binary search is only applicable in a sorted search space. 
    The sorted search space does not necessarily have to be a sorted array. 
    It can be anything but the search space must be sorted.
    In binary search, we generally divide the search space into two equal halves and then try to locate which half contains the target. According to that, we shrink the search space size.
    
    algo:
    
    mid = (low+high)/2
    possible conditions: 
    if arr[mid] == target => return mid
    if arr[mid]<target => target is to right side => low = mid+1
    if arr[mid]>target = > target is to left side => high = mid-1
    ~
    """
    low = 0
    high = len(arr)-1
    while(low<=high):
        mid = (low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low = mid+1
        else:
            high = mid-1
    return -1



if __name__=='__main__':
    arr = [2, 100, 120, 150]
    target = 120
    
    print(search(arr, target))  