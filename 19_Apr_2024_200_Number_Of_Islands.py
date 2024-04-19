class Solution:
    #TC: O(N*M) SC: O(1) 
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        n, m=  len(grid), len(grid[0])
        def dfs(i,j):
            if i>=n or j>=m or i<0 or j<0 or grid[i][j]== '0':
                return 
            
            # print(i,j)
            grid[i][j]= '0'
            
            dfs(i+1, j)
            dfs(i, j+1)
            dfs(i-1, j)
            dfs(i, j-1)
        
        
        for i in range(n):
            for j in range(m):
                if grid[i][j]=='1':
                    dfs(i,j)
                    ans+=1
                    
        return ans
