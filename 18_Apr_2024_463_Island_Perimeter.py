class Solution:
    #TC: O(N*M) SC: O(1)
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0
        di= [(0,1), (1,0), (-1,0), (0,-1)]
        n, m=  len(grid), len(grid[0])
        def dfs(i,j):
            if i>=n or j>=m or i<0 or j<0 or (grid[i][j]== 0 or grid[i][j]==-1):
                return 0
            # print(i,j)
            
            grid[i][j]= -1
            p= 4
            for d in di:
                if i+d[0] < n and j+ d[1]< m and i+d[0]>=0 and j+ d[1]>=0 and (grid[i+d[0]][j+d[1]]==1 or grid[i+ d[0]][j+d[1]]== -1):
                    p-=1
            
            
            p+= dfs(i+1, j)
            p+= dfs(i, j+1)
            p+= dfs(i-1, j)
            p+= dfs(i, j-1)
            
            return p
        
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    return dfs(i,j)
                
        return 0
