#User function Template for python3
class Solution:
    def maxConsecutiveCount(self, arr):
        max_count = 0
        cur_count = 1
        for i in range(1,len(arr)):
            if arr[i] == arr[i-1]:
                cur_count += 1
            else:
                max_count = max(max_count,cur_count)
                cur_count = 1
        max_count = max(max_count,cur_count)
        return max_count
            
                
                
                
                


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.maxConsecutiveCount(arr)
        print(ans)
        print("~")
# } Driver Code Ends