"""  
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

"""
Observations:
1. The number of distinct ways to climb to the top can be represented as a Fibonacci-like sequence.
2. The number of ways to reach step n is the sum of the ways to reach step n-1 and step n-2.
"""
def climb_stairs(n: int) -> int:
    """
    Thought Process:
    IBH Method:
    1. Induction: We need to find the number of distinct ways to climb n steps.
    2. Base Condition: If n is 0 or 1, return 1 (only one way to stay at the ground or take one step).
    3. Hypothesis: Assume we can find the number of ways to climb n-1 and n-2 steps.
    4. Induction Step: Use the hypothesis to find the number of ways to climb n steps.
    Time Complexity: O(n) - Linear time complexity due to the iterative approach.
    Space Complexity: O(1) - Constant space used for variables.
    5. Edge Cases: If n is negative, return 0.
    """
    if n <= 1:
        return n 
    return climb_stairs(n - 1) + climb_stairs(n - 2)

def climb_stairs_memo(n: int, memo=None) -> int:
    """
    Thought Process:
    Use in-memory caching to store previously computed results.
    """
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = climb_stairs_memo(n - 1, memo) + climb_stairs_memo(n - 2, memo)
    return memo[n]

def climb_stairs_dp(n: int) -> int:
    """
    Thought Process:
    Use dynamic programming to iteratively compute the number of ways to climb stairs.
    """
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

def climb_stairs_optimized(n: int) -> int:
    """
    Thought Process:
    Use two variables to keep track of the last two computed values to save space.
    """
    if n <= 1:
        return n

    prev1, prev2 = 1, 1

    for _ in range(2, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current

    return prev1
if __name__ == "__main__":
    n = 10
    print(f"Number of distinct ways to climb {n} steps (Recursive): {climb_stairs(n)}")
    print(f"Number of distinct ways to climb {n} steps (Memoization): {climb_stairs_memo(n)}")
    print(f"Number of distinct ways to climb {n} steps (Dynamic Programming): {climb_stairs_dp(n)}")
    print(f"Number of distinct ways to climb {n} steps (Optimized DP): {climb_stairs_optimized(n)}")
