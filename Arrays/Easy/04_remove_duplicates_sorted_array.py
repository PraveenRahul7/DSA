""" 
You are given a sorted integer array 'arr' of size 'n'.


You need to remove the duplicates from the array such that each element appears only once.


Return the length of this new array.


Note:

Do not allocate extra space for another array. You need to do this by modifying the given input array in place with O(1) extra memory. 


For example:

'n' = 5, 'arr' = [1 2 2 2 3].
The new array will be [1 2 3].
So our answer is 3.


"""
from typing import List

def remove_duplicates(arr: List[int])->int:
    """
        Logic: Track Index of unique elements, Move the unique element to the front. 
    """
    
    if not arr:
        return 0
    
    res = 0
    for i in range(1, len(arr)):
        if arr[i] != arr[res]:
            res += 1
            arr[res] = arr[i]
    return res+1
         
    
                    
if __name__=='__main__':
    try:
        arr = list(map(int, input().split()))
        print(remove_duplicates(arr))
    except ValueError as e:
        print(f"Error: {e}")