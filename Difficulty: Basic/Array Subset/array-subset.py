#User function Template for python3
from collections import Counter
class Solution:
   
    def isSubset(self, a, b):
        freq_a = Counter(a)
        freq_b = Counter(b)
        for num in freq_b:
            if freq_b[num] > freq_a[num]:
                return False
            
            
        return True

    
    
    
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):
        a1 = [int(x) for x in input().strip().split()]
        a2 = [int(x) for x in input().strip().split()]
        ob = Solution()
        if ob.isSubset(a1, a2):
            print("true")
        else:
            print("false")

        T -= 1

        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends