class Solution:
    #TC: O(M*N) SC: O(1)
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        
        m, n = len(grid1), len(grid1[0])
        di = [(0,1), (1,0), (-1,0), (0,-1)]
        
        def dfs(i, j):
            nonlocal flag
            if grid1[i][j] == 0:
                flag= False
                
            grid2[i][j] = -1
            
            for d in di:
                newi = i+ d[0]
                newj = j+ d[1]
                if newi>=0 and newi< m and newj>=0 and newj < n and grid2[newi][newj]== 1:
                    dfs(newi, newj)
            
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid2[i][j]== 1:
                    flag= True
                    dfs(i, j)
                    if flag:
                        ans+=1
                    
        return ans
