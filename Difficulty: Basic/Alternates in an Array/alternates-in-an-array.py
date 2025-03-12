#User function Template for python3
class Solution:
    def getAlternates(self, arr):
        result = []
        for i in range(len(arr)):
            if i % 2 == 0:
                result.append(arr[i])
        return result
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3
t = int(input())
for i in range(t):
    arr = list(map(int, input().split()))
    ls = Solution().getAlternates(arr)
    print(" ".join(map(str, ls)))
    print("~")

# } Driver Code Ends