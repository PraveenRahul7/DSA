""" 
You are given an array 'a' of 'n' integers.


A majority element in the array 'a' is an element that appears more than 'n' / 2 times.


Find the majority element of the array.


It is guaranteed that the array 'a' always has a majority element.


Example:

Input: 'n'= 9, 'a' = [2, 2, 1, 3, 1, 1, 3, 1, 1]

Output: 1

Explanation: The frequency of'1' is 5, which is greater than 9 / 2.
Hence '1' is the majority element.

"""

""" 
Moore Voting Algo Intution:

Intuition:

If the array contains a majority element, its occurrence must be greater than the floor(N/2). Now, we can say that the count of minority elements and majority elements is equal up to a certain point in the array. So when we traverse through the array we try to keep track of the count of elements and the element itself for which we are tracking the count. 

After traversing the whole array, we will check the element stored in the variable. If the question states that the array must contain a majority element, the stored element will be that one but if the question does not state so, then we need to check if the stored element is the majority element or not. If not, then the array does not contain any majority element.
Approach: 

    Initialize 2 variables:
    Count =>  for tracking the count of element
    Element => for which element we are counting
    Traverse through the given array.
        If Count is 0 then store the current element of the array as Element.
        If the current element and Element are the same increase the Count by 1.
        If they are different decrease the Count by 1.
    The integer present in Element should be the result we are expecting 

"""
from typing import List


def moore_voting_algo_majority_element(arr:List[int])->int:
    count=0
    element=None
    for num in arr:
        if count==0:
            element = num
            count+=1
        elif num == element:
            count+=1
        else:
            count-=1
    return element
    

if __name__=='__main__':
    arr = [2, 2, 1, 3, 1, 1, 3, 1, 1]
    print(moore_voting_algo_majority_element(arr))  