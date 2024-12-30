""" 
You have been given an array a of a unique non-negative integers.


Find the second largest and second smallest element from the array.


Return the two elements (second largest and second smallest) as another array of size 2.


Example :

Input: n = 5, a = [1, 2, 3, 4, 5]
Output: [4, 2]

The second largest element after 5 is 4, and the second smallest element after 1 is 2.


"""

from typing import List

def getSecondOrderElements(arr: List[int])->List[int]:
    if len(arr)<2:
        return []
    
    largest = float('-inf')
    smallest = float('inf')
    second_largest = float('-inf')
    second_smallest = float('inf')
    
    for num in arr: 
        if num>largest:
            second_largest = largest
            largest = num
        elif num>second_largest and num!=largest:
            second_largest = num
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num<second_smallest and second_smallest!=smallest:
            second_smallest = num
                
    return [second_largest, second_smallest]
    
                    
    
        
        
            
if __name__=='__main__':
    try:
        arr = list(map(int, input().split()))
        print(getSecondOrderElements(arr))
    except ValueError as e:
        print(f"Error: {e}")