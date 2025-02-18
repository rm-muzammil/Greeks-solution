#User function Template for python3
class Solution:
    def getSecondLargest(self, arr):
        largest = max(arr)
        new_arr = [-1]
        for num in arr:
            if num != largest:
                new_arr.append(num)
        sec_large = max(new_arr)
        if sec_large < largest:
            return sec_large
        else:
            return -1


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSecondLargest(arr)
        print(ans)
        print("~")
# } Driver Code Ends