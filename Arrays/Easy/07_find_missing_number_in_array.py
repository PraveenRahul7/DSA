""" 
Given an array a of size n-1 with elements of range 1 to n. The array does not contain any duplicates. Your task is to find the missing number.


For example:

Input:
'a' = [1, 2, 4, 5], 'n' = 5

Output :
3

Explanation: 3 is the missing value in the range 1 to 5.


"""

from typing import List

def find_missing_number(arr:List[int], n:int)->int:
    sum = n*(n+1)//2 # sum(range(1,n+1))
    arr_sum = 0
    for num in arr:
        arr_sum += num
    return sum-arr_sum


def find_missing_number_using_xor(arr:List[int], n:int)->int:
    """
    XOR of all arr elements ->arr_xor
    XOR of 1 to n -> num_xor
    
    res = arr_xor ^ num_xor
    
    """
    arr_xor, num_xor = 0,0
    for ele in arr:
        arr_xor ^= ele
    for num in range(1, n+1):
        num_xor ^= num
    
    return arr_xor ^ num_xor
        
            
        
        


if __name__=='__main__':
    arr = [1, 2, 4, 5]
    n = 5
    # print(find_missing_number(arr, n))
    print(find_missing_number_using_xor(arr, n))