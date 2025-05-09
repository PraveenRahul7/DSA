""" 
Sort a stack using recussion.

"""
def insert(arr, temp):
    if len(arr) == 0 or arr[-1]>=temp:
        #Base Condition: If len of arr is 0, then put temp or if last elemnt in arr is <= temp then put temp. Once we get arr[-1] <=temp we are done with insert so it has to be in base-condition
        arr.append(temp)
        return
    last_element = arr.pop()
    insert(arr, temp) #This will insert the temp at correct position
    arr.append(last_element) #At last put last element to end (its correct position)
    
    

def sortArray(arr):
    if len(arr) == 1:
        return
    temp = arr.pop() # Induction: Work for last element
    sortArray(arr) #This will give me sorted array from 0..n-1
    insert(arr, temp) #Place the temp at correct position
    



if __name__ == "__main__":
    arr = [2,3, 1, 4, 5, 5, 0, 2, 1, 9, 7] 
    # Ideal Print: 7 9 1 2 0 5 5 4 1 3 2
    # Sorted Print: 9 7 5 5 4 3 2 2 1 1 0
    sortArray(arr)
    print(arr)