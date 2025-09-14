#User function Template for python3

class Solution:
    def getTable(self,n):
        arr = []
        for num in range(1,11):
            arr.append(num*n)
        return arr
            