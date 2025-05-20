class Solution:
    #TC: O(N) SC: O(N)
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        prefix = [0] * (n+1)
        for l,r in queries:
            prefix[l]-=1
            prefix[r+1] +=1

        s = 0
        for i in range(n):
            s+= prefix[i]
            nums[i] += s

        print(nums)
        if all(num <= 0 for num in nums):
            return True
        return False
