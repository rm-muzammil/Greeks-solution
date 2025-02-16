#User function template for Python 3

class Solution:
    import math
    def majorityElement(self, arr):
        arr.sort()
        can, count = None, 0
        for num in arr:
            if count == 0:
                can = num
            count += (1 if num == can else -1)
        if arr.count(can) > len(arr) // 2:
            return can
        else:
            return -1
            
        
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

from sys import stdin


def main():
    T = int(input())
    while (T > 0):

        A = [int(x) for x in input().strip().split()]

        obj = Solution()
        print(obj.majorityElement(A))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends