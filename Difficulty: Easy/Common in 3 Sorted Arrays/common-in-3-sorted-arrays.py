#User function Template for python3

class Solution:
    def commonElements(self, arr1, arr2, arr3):
        n1 = len(arr1)
        n2 = len(arr2)
        n3 = len(arr3)
        i,j,k = 0,0,0
        result = []
        
        while i < n1 and j < n2 and k < n3:
            # If all three elements are equal, add to result
            if arr1[i] == arr2[j] == arr3[k]:
                if not result or result[-1] != arr1[i]:  # Avoid duplicates
                    result.append(arr1[i])
                i += 1
                j += 1
                k += 1
            
            # Move the pointer with the smallest value
            elif arr1[i] < arr2[j]:
                i += 1
            elif arr2[j] < arr3[k]:
                j += 1
            else:
                k += 1
        
        return result if result else [-1] 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        brr = list(map(int, input().split()))
        crr = list(map(int, input().split()))
        ob = Solution()
        res = ob.commonElements(arr, brr, crr)
        if len(res) == 0:
            print(-1)
        else:
            print(" ".join(map(str, res)))
        print("~")
# } Driver Code Ends