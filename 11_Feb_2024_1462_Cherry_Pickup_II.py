class Solution:
    #TC: O(M*M*N) SC: O(M*M*N)
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n, m= len(grid), len(grid[0])
        dp= [[[-1]* m for _ in range(m)] for __ in range(n)]
        def recur(i, j1, j2):
            if i >=n or j1>=m or j1< 0 or j2>=m or j2< 0:
                return 0
            
            if dp[i][j1][j2]!=-1:
                return dp[i][j1][j2]
            
            d= [-1, 0, 1]
            ans = 0
            for d1 in d:
                for d2 in d:
                    ans= max(ans, recur(i+1, j1+ d1, j2+ d2))
            
            if j1 == j2:
                dp[i][j1][j2] =  grid[i][j1]+ ans
            else:
                dp[i][j1][j2] = grid[i][j1]+ grid[i][j2]+ ans
            return dp[i][j1][j2]
        
        return recur(0, 0, m-1)
