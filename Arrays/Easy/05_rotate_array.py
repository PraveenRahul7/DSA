""" 
Given an array 'arr' containing 'n' elements, rotate this array left once and return it.


Rotating the array left by one means shifting all elements by one place to the left and moving the first element to the last position in the array.


Example:

Input: 'a' = 5, 'arr' = [1, 2, 3, 4, 5]

Output: [2, 3, 4, 5, 1]

Explanation: We moved the 2nd element to the 1st position, and 3rd element to the 2nd position, and 4th element to the 3rd position, and the 5th element to the 4th position, and move the 1st element to the 5th position.

"""
from typing import List
def left_rotate_by_one(arr:List[int])->List[int]:
    
    # Alternate Way : return arr[1:] + arr[:1]
    first_element = arr[0]
    for i in range(1, len(arr)):
        arr[i-1] = arr[i-1]
    arr[-1] = first_element
    return arr
     
def rotate(arr: List[int], i, j)->None:
    while(i<j):
        arr[j], arr[i] = arr[i], arr[j]
        j-=1
        i+=1
    
    
def left_rotate_by_d(arr: List[int], d:int)->List[int]:
    """ 
    rotate(arr, 0, d-1)
    rotate(arr, d, n-1)
    rotate(arr, 0, n-1)
    """
    rotate(arr, 0, d-1)
    rotate(arr, d, len(arr)-1)
    rotate(arr, 0, len(arr)-1)
    return arr

if __name__=='__main__':
    try:
        arr = list(map(int, input().split()))
        d = int(input())
        # print(left_rotate_by_one(arr))
        print(left_rotate_by_d(arr, d))
    except ValueError as e:
        print(f"Error: {e}")