""" 
You're given a sorted array 'a' of 'n' integers and an integer 'x'.


Find the floor and ceiling of 'x' in 'a[0..n-1]'.


Note:

Floor of 'x' is the largest element in the array which is smaller than or equal to 'x'.
Ceiling of 'x' is the smallest element in the array greater than or equal to 'x'.


Example:

Input: 
n=6, x=5, a=[3, 4, 7, 8, 8, 10]   

Output:
4

Explanation:
The floor and ceiling of 'x' = 5 are 4 and 7, respectively.

"""

""" 
floor: largest element less than x

if arr[mid] == x -> return mid

arr[mid]<x => we will get possible answer.

res = -1
keep on updaing res inside arr[mid]<x
if arr[mid]<x:
    res = mid
    start = mid+1

ceil : smallest element greater than x

if arr[mid] == x : return mid.

if arr[mid]>x => do work. 
res = -1

if arr[mid]>x : 
    res = mid
    high = mid-1

"""

def getFloorAndCeil(a, n, x):
    # Write your code here.
    floor, ceil = -1, -1
    low, high = 0, n - 1

    while low <= high:
        mid = (low + high) // 2

        if a[mid] == x:
            # If the element is found, floor and ceil are the same
            return [a[mid], a[mid]]
        elif a[mid] < x:
            # Update floor to the current mid value
            floor = a[mid]
            low = mid + 1
        else:
            # Update ceil to the current mid value
            ceil = a[mid]
            high = mid - 1

    return [floor, ceil]
