class Solution:
    #TC: O(N*M*N*M) SC: O(N*M)
    def minDays(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        visited = [[False]* n for _ in range(m)]
        di = [(0,1), (1,0), (0,-1), (-1, 0)]
        
        def dfs(i, j):
            visited[i][j]= True
            for d in di:
                newx = i+ d[0]
                newy = j+ d[1]
                
                if newx>=0 and newx <m and newy>=0 and newy<n and grid[newx][newy]!=0 and not visited[newx][newy]:
                    dfs(newx, newy)
                    
         
        def cntIslands():
            islands = 0
            for i in range(m):
                for j in range(n):
                    if grid[i][j]==1 and not visited[i][j]:
                        dfs(i, j)
                        islands+=1
                        
            return islands
        
        if cntIslands() == 1:
            for i in range(m):
                for j in range(n):
                    if grid[i][j]==1:
                        grid[i][j] = 0
                        visited = [[False]* n for _ in range(m)]
                        islands = cntIslands()
                        if islands !=1:
                            return 1
                        
                        grid[i][j] = 1
            return 2            
        else:
            return 0
                    
            
            
