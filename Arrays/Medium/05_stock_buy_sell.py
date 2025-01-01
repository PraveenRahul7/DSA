""" 
You are given an array/list 'prices' where the elements of the array represent the prices of the stock as they were yesterday and indices of the array represent minutes. Your task is to find and return the maximum profit you can make by buying and selling the stock. You can buy and sell the stock only once.

Note:

You can’t sell without buying first.

For Example:

For the given array [ 2, 100, 150, 120],
The maximum profit can be achieved by buying the stock at minute 0 when its price is Rs. 2 and selling it at minute 2 when its price is Rs. 150.
So, the output will be 148.



"""
from typing import List

def maximumProfit(arr:List[int])->int:
    # # Logic: Cumulative Sum
    # profit = 0
    # for i in range(1, len(arr)):
    #     if arr[i]>arr[i-1]:
    #         profit+=(arr[i]-arr[i-1])
    
    # return profit
    
    """ 
        Intuition: We will linearly travel the array. We can maintain a minimum from the start of the array and compare it with every element of the array, if it is greater than the minimum then take the difference and maintain it in max, otherwise update the minimum.
    
    """
    maxPro = 0
    minPrice = float('inf')
    for i in range(len(arr)):
        minPrice = min(minPrice, arr[i])
        maxPro = max(maxPro, arr[i] - minPrice)
    return maxPro

        
    

if __name__=='__main__':
    arr = [2, 100, 150, 120]
    print(maximumProfit(arr))  