class Solution:
    #TC: O(N^2 LOGN) SC: O(N^2)
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        n = len(nums)
        mod = 10**9 + 7
        sums = []
        
        for i in range(n):
            s = 0
            for j in range(i, n):
                s+= nums[j]
                sums.append(s)
                
        sums.sort()
        res = 0
        for i in range(left - 1, right):
            res+= sums[i]
            res%= mod
            
        return res
