class Solution:
    #TC: O(N*M) SC: O(1)
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        
        di = [(0,1), (0,-1), (-1,0), (1,0)]
        def dfs(i, j):
            
            val = newgrid[i][j]
            newgrid[i][j] = -1
            
            ans = 0
            for d in di:
                newi= i+ d[0]
                newj= j+ d[1]
                
                if newi< m and newi>=0 and newj< n and newj>=0 and newgrid[newi][newj] > 0:
                    ans= max(ans, dfs(newi, newj))
                    
            newgrid[i][j]= val
            return val+ ans
        
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]> 0:
                    newgrid = copy.deepcopy(grid)
                    res= max(res, dfs(i,j))
                
        return res
        
        
            
            
