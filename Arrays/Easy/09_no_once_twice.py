""" 
You are given a sorted array 'arr' of positive integers of size 'n'.


It contains each number exactly twice except for one number, which occurs exactly once.


Find the number that occurs exactly once.


Example :

Input: 'arr' = {1, 1, 2, 3, 3, 4, 4}.

Output: 2

Explanation: 1, 3, and 4 occur exactly twice. 2 occurs exactly once. Hence the answer is 2.

Detailed explanation ( Input/output format, Notes, Images ) 

"""

from typing import List
from functools import reduce

def getSingleElement(arr:List[int])->int:
    # return reduce(lambda x,y: x^y, arr)
    

    # Declare the hashmap.
    # And hash the given array:
    hashmap = {}
    for num in arr:
        hashmap[num] = hashmap.get(num, 0) + 1

    # Find the single element and return the answer:
    for num, count in hashmap.items():
        if count == 1:
            return num
    
        
            
        
    

if __name__=='__main__':
    arr = [1, 1, 2, 3, 3, 4, 4]
    print(getSingleElement(arr))    