class Solution:
    #TC: O(N) SC: O(N)
    def rob(self, nums: List[int]) -> int:
        n= len(nums)
        dp = [0]*(n+1)
        dp[1]= nums[0]
        if n==1: return dp[1]
        
        for i in range(1,n+1):
            dp[i]= max(dp[i-1],nums[i-1]+dp[i-2])
        return dp[n]
