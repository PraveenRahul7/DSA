""" 
Delete middle of stack

"""
def deleteMiddleStack(s, k):
    if k==1:
        s.pop()
        return 
    top = s.pop()
    deleteMiddleStack(s, k-1)
    s.append(top)

def deleteMiddle(inputStack, N):

    # Write your solution here
    if len(inputStack) == 0:
        return inputStack
    middle = (N//2)+1
    deleteMiddleStack(inputStack, middle)
    return inputStack



if __name__ == "__main__":
    arr = [2,3, 1, 4, 5, 5, 0, 2, 1, 9, 7] 
    # Ideal Print: 7 9 1 2 0 5 5 4 1 3 2
    # Sorted Print: 9 7 5 5 4 3 2 2 1 1 0
    N = len(arr)-1
    deleteMiddle(arr, N)
    print(arr)