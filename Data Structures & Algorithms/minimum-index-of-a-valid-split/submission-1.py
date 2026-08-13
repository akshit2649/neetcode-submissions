from collections import defaultdict
class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        freq = defaultdict(int)
        n = len(nums)
        
        for i in nums:
            freq[i] += 1
        
        dom = None
        for k,v in freq.items():
            if 2 * v > n:
                dom = k    
                break

        pre, suf = [0] * n, [0] * n

        for i in range(n):
            if nums[i] == dom:
                pre[i] += 1
            if i != 0:
                pre[i] += pre[i-1]
        
        for i in range(n-1, -1, -1):
            if nums[i] == dom:
                suf[i] += 1
            if i != n-1:
                suf[i] += suf[i+1]
        
        print(pre)
        print(suf)
        for i in range(n-1):
            if (2 * pre[i] > i+1) and (2 * suf[i+1] > n - (i+1)):
                return i

        return -1



        