class Solution:
    def findSum(self, n):
        result =0
        while n > 0:
            result+=n
            n-=1
        return result
        
