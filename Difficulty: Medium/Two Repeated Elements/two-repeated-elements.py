#User function Template for python3

class Solution:
    
    #Function to find two repeated elements.
    def twoRepeated(self, n, arr):
        result = []
        seen = set()
        for num in arr:
            if num in seen:
                result.append(num)
                if len(result) == 2:
                    break
            seen.add(num)
        return tuple(result)
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        n = int(input())

        arr = [int(x) for x in input().strip().split()]

        obj = Solution()
        ans = obj.twoRepeated(n, arr)
        print(ans[0], ans[1])

        T -= 1

        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends