#User function Template for python3

class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        n = len(arr)
        d %=n
        arr[:d] = reversed(arr[:d])
        arr[d:] = reversed(arr[d:])
        arr[:] = reversed(arr)