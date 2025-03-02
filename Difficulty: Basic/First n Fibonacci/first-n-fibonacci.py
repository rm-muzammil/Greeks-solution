#User function Template for python3

class Solution:
    #Function to return list containing first n fibonacci numbers.
    def fibonacciNumbers(self,n):
        if n == 0:
            return []
        if n == 1:
            return [0]
        fib = [0,1]
        for _ in range(2,n):
            fib.append(fib[-1] + fib[-2])
        return fib
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    t = int(input())
    for tcs in range(t):

        n = int(input())
        res = Solution().fibonacciNumbers(n)
        for i in range(len(res)):
            print(res[i], end=" ")
        print()
        print("~")

# } Driver Code Ends