class Solution:
    # TC: O(N * SUM(NUMS)) SC: O(N* (SUM(NUMS)))
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        n = len(nums)
        if s % 2:
            return False
        
        @cache
        def recur(idx, target):
            if target == 0:
                return True

            if idx == n or target < 0:
                return False

            return recur(idx+1, target- nums[idx]) or recur(idx+1, target)

        return recur(0, s//2)
