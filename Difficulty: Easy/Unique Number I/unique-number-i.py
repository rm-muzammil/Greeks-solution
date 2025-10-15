class Solution:
    def findUnique(self, arr):
        cnt = {}
        for num in arr:
            cnt[num] = cnt.get(num,0)+1
        for key,value in cnt.items():
            if value == 1:
                return key
        return -1