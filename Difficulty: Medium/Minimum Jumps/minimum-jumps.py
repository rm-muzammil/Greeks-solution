class Solution:
    def minJumps(self, arr):
        n = len(arr)
        if n == 1:
            return 0
        if arr[0] == 0:
            return -1
        
        jumps = 0
        farthest = 0
        current_end = 0

        for i in range(n - 1):  # No need to check the last element
            farthest = max(farthest, i + arr[i])
            
            if i == current_end:  # Time to make a jump
                jumps += 1
                current_end = farthest
                if current_end >= n - 1:  # If reached or exceeded the last index
                    return jumps
        
        return -1  # If we never reach the last index



#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        # n = int(input())
        Arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.minJumps(Arr)
        print(ans)
        print("~")
# } Driver Code Ends