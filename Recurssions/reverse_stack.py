#User function Template for python3

from typing import List

class Solution:
    def insert(self, St, k):
        if len(St)==0:
            St.append(k)
            return
        top = St.pop() #Remove top element
        self.insert(St, k) #This will give me reversed element in correct order till n-1
        # as n-1 elements are already reversed, I just need to add top element back to its top. 
        St.append(top)
        
    def reverse(self,St): 
        #code here
        if len(St)==0:
            return
        top = St.pop() #Need to do work on top element
        self.reverse(St) #Hypothesis: This will give me reversed stack of n-1 elements 
        # I just need to insert this top element at correct position
        self.insert(St, top)