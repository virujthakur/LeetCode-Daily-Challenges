class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n= len(jobDifficulty)
        if n < d:
            return -1
        
        dp= [[-1]* (d+1) for i in range(n)]
        
        def recur(idx, days):
            if idx== n and days == 0:
                return 0
            
            if days == 0 or idx== n:
                return 10** 9
            
            if dp[idx][days]!=-1:
                return dp[idx][days]
            
            mxDiff = 0
            ans = 10 ** 9
            for j in range(idx, n):
                mxDiff= max(jobDifficulty[j], mxDiff)
                ans= min(ans, mxDiff+ recur(j+1, days-1))
            
            dp[idx][days]= ans
            return ans
        
        return recur(0, d)
            
            
        
