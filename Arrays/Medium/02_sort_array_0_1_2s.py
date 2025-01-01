""" 
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

"""

from typing import List

def sort_array(arr:List[int])->None:
    """ 
    Apply Dutch National Flag Algorithm.
    
    Three Pointers:
        1. low -> count of 0's (from 0 to low-1)
        2. mid -> count of 1's (from low to mid-1)
        3. high -> count of 2's (from high+1 to n-1)
        
                arr[0….low-1] contains 0. [Extreme left part]
                arr[low….mid-1] contains 1.
                arr[high+1….n-1] contains 2. [Extreme right part], n = size of the array
        
        Assume that 
            - all elements from 0...low-1 are 0's,
            - all elements from low to mid-1 are 1's
            - all elements from high+1 to n-1 are 2's.
            
            So, all elements from mid to high are unsorted => Work needs to be done to sort elements b/w mid and high. 
        
                
        Algo: 
        
        initially, 
        low=0, mid = 0 and high = n-1 => So hypothetically  elements from mid to high are unsorted.
        while(mid<=high) -> 
            if arr[mid] is 0 then swap arr[mid] and arr[low] and then increment low and mid => this way we push 0's to beginning and low will have count of 0's.
            
            if arr[mid] is 1 the just increment count of mid as mid stores count of 1's. 
            
            if arr[mid] is 2, then swap arr[mid] with arr[high] and decrement high as we need to store count of 2's b/w high+1 to n-1.
    """
    low, mid = 0, 0
    high = len(arr)-1
    
    while(mid<=high):
        if(arr[mid]==0):
            arr[mid], arr[low] = arr[low], arr[mid]
            low+=1
            mid+=1
        elif(arr[mid]==1):
            mid+=1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high-=1
    return arr

if __name__=='__main__':
    arr = [2,0,2,1,1,0]
    print(sort_array(arr))  