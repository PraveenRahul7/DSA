""" 
Given an array arr[ ] of integers, the task is to find the next greater element for each element of the array in order of their appearance in the array. Next greater element of an element in the array is the nearest element on the right which is greater than the current element.
If there does not exist next greater of current element, then next greater element for current element is -1. For example, next greater of the last element is always -1.

Examples

Input: arr[] = [1, 3, 2, 4]
Output: [3, 4, 4, -1]
Explanation: The next larger element to 1 is 3, 3 is 4, 2 is 4 and for 4, since it doesn't exist, it is -1.

Input: arr[] = [6, 8, 0, 1, 3]
Output: [8, -1, 1, 3, -1]
Explanation: The next larger element to 6 is 8, for 8 there is no larger elements hence it is -1, for 0 it is 1 , for 1 it is 3 and then for 3 there is no larger element on right and hence -1.

Input: arr[] = [10, 20, 30, 50]
Output: [20, 30, 50, -1]
Explanation: For a sorted array, the next element is next greater element also exxept for the last element.

Input: arr[] = [50, 40, 30, 10]
Output: [-1, -1, -1, -1]
Explanation: There is no greater element for any of the elements in the array, so all are -1.

Constraints:
1 ≤ arr.size() ≤ 106
0 ≤ arr[i] ≤ 109


"""



""" 
Observations:

1. The next greater of last element is always -1.
2. Brute force: 
    for i in range(0, len(arr)):
        for j in range(i, len(arr)):
            ...computataion...
=> if inner loop depends on outer loop -> Think of using a stack!!!, because i requires the computation of j's work and we can store them in a ds like stack.

3. In this problem, we need to keep track of next greater of each element in the array. Think of using a two-pointers
    
-> Two pointers won't work effectively for problems like Next Greater Element in O(N) time because the relationship between elements isn't sequential—it requires looking ahead or maintaining a context of multiple potential candidates.
    
-> Two pointers can't "remember" previous elements efficiently. Once a pointer moves past an element, that element's information is lost unless explicitly stored (e.g., in a stack).

-> The stack's ability to "remember" and process potential candidates in a single pass makes it the optimal solution.
"""

""" 
Key Idea:

When the inner loop depends on the outer loop for computations (e.g., j depends on i), it often indicates that you are recalculating or reprocessing information unnecessarily. Using a stack (or another data structure) allows you to store partial results or states as you process elements, avoiding redundant calculations.


When to Think of a Stack:

    Inner loop depends on the outer loop's work.
        E.g., for i, for j inside depends on values seen before or after.
    Problems that involve relationships between elements:
        Next Greater Element: Find the nearest larger element to the right.
        Histogram Problems: Find the largest rectangle in a histogram.
        Balanced Parentheses: Check if parentheses are well-formed.
        Monotonic Sequence: Maintain order while processing.

General Rule:

If the inner loop depends on the work of the outer loop, and you notice redundant computations, try using a stack to manage intermediate results or states efficiently. This reduces the complexity and often simplifies the logic.

"""


""" solve next greater element: 

    res = []
    stack = []
    
    1. If Stack is empty : -1
    2. If stack is not empty and stack.top <=arr[i]=> not useefull -> pop them, key idea is always put greater to res.
    3. if stack is not empty and stack.top>arr[i] => usefull -> add them

"""

class Solution:
    # Function to find the next greater element for each element of the array.
    def nextLargerElement(self, arr):
        # code here
        stack = []
        res = []
        for i in range(len(arr)-1, -1, -1):
            while stack and stack[-1]<=arr[i]:
                stack.pop()
            if stack:
                res.append(stack[-1])
            else:
                res.append(-1)
            stack.append(arr[i])
        res.reverse()
        return res