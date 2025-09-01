#User function Template for python3
class Solution:
    def subarraySum(self, arr, target):
        start = 0
        curr_sum = 0
        n = len(arr)
        for end in range(0,n):
            curr_sum += arr[end]
            
            while curr_sum > target and start < end:
                curr_sum -= arr[start]
                start += 1
            if curr_sum == target:
                return [start + 1, end + 1]
        return [-1]