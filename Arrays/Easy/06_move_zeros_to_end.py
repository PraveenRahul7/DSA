""" 

Given an array 'arr' of 'n' non-negative integers, your task is to move all the zeros to the end of the array while keeping the non-zero elements at the start of the array in their original order. 
Return the modified array.


Example :

Input: n = 5, arr = [1, 2, 0, 0, 2, 3]
Output: [1, 2, 2, 3, 0, 0]

Explanation: Moved all the 0's to the end of an array, and the rest of the elements retain the order at the start.

"""

from typing import List

def move_zeros_end(arr:List[int])->List[int]:
    """ 
    Logic: Track count of non zero elements and swap non-zero element with arr[count]
    T.C : O(N)
    S.C : O(1)
    """
    if not arr:
        return arr
    idx = 0
    for i in range(0, len(arr)):
        if arr[i] != 0:
            arr[i], arr[idx] = arr[idx], arr[i]
            idx += 1
    return arr
            
        
        


if __name__=='__main__':
    arr = [1, 2, 0, 0, 2, 3]
    print(move_zeros_end(arr))