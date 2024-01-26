class Solution:
    def findPaths(self, m: int, n: int, mM: int, sR: int, sC: int) -> int:
        mod= 10**9 + 7
        dp= [[[-1]* (mM+1) for _ in range(n)] for _ in range(m)]
        def dfs(i,j,mov):
            if i<0 or j<0 or i>=m or j>=n:
                return 1
            if mov==0:
                return 0
            
            if dp[i][j][mov]!= -1:
                return dp[i][j][mov]
            ans= 0
            ans += dfs(i+1,j,mov-1)
            ans += dfs(i,j+1,mov-1)
            ans += dfs(i-1,j,mov-1)
            ans += dfs(i,j-1,mov-1)
            
            dp[i][j][mov]= ans % mod
            return ans % mod
        
        return dfs(sR, sC, mM)
