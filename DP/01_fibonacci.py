"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).

 

Example 1:

Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
Example 2:

Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
Example 3:

Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.

"""

""" 
Here there is a repetative work of calculating the fibonacci numbers.
Like, at any i, we compute F(i-1) and F(i-2) and then add them.
So, we can use dynamic programming to store the results of F(i-1) and F(i-2) in a list and use them to compute F(i) without recomputing them again.

"""

#Normal Recursion:
def fib(n: int) -> int:
    """
    Thought Process:
    IBH Method:
    1. Induction: We need to find the nth Fibonacci number.
    2. Base Condition: If n is 0 or 1, return n.
    3. Hypothesis: Assume we can find the Fibonacci numbers for n-1 and n-2.
    4. Induction Step: Use the hypothesis to find the Fibonacci number for n.   
    Time Complexity: O(2^n) - Exponential time complexity due to the recursive calls.
    Space Complexity: O(n) - Space used by the call stack.
    5. Edge Cases: If n is negative, return 0.
    """
    if n<=1:
        return n
    return fib(n-1) + fib(n-2)

#Memoization/ Top Down Approach:
def fib_memo(n: int, memo=None) -> int:
    """
    Thought Process:
    Use in-memory caching to store previously computed Fibonacci numbers.
    """
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    
    return memo[n]

#Tabulation/ Bottom Up Approach:
def fib_tab(n: int) -> int:
    """
    Thought Process:
    Use a bottom-up approach to build the Fibonacci sequence iteratively.
    """
    if n <= 1:
        return n

    fib = [0] * (n + 1)
    fib[0], fib[1] = 0, 1

    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]

if __name__ == "__main__":
    n = 10
    print(f"Fibonacci of {n} using normal recursion: {fib(n)}")     
    print(f"Fibonacci of {n} using memoization: {fib_memo(n)}")
    print(f"Fibonacci of {n} using tabulation: {fib_tab(n)}")
