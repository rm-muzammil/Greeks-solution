#User function Template for python3

class Solution:

    def convert(self, s):
        result = []
        for ch in s:
            if 'a' <= ch <= 'z':
                result.append(chr(219-ord(ch)))
            # elif 'A' <= ch <= 'Z':
            else:
                result.append(chr(155-ord(ch)))
                # result.append(ch)
        return "".join(result)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        ans = solObj.convert(s)

        print(ans)
        print("~")
# } Driver Code Ends