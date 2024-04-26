class Solution:
    # TC: O(N^2) SC: O(N^2)
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n= len(grid)
        dp= [[-1]*(n+1) for _ in range(n)]
        
        def recur(i, prev):
            if i == n:
                return 0
            
            if dp[i][prev+1]!= -1:
                return dp[i][prev+1]
            
            ans = 10**9
            for j in range(n):
                if j!= prev:
                    ans= min(ans, grid[i][j]+ recur(i+1, j))
            
            dp[i][prev+1]= ans
            return ans
        
        return recur(0, -1)
            
