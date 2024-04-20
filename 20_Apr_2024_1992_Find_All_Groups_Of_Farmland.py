class Solution:
    #TC: O(N*M) SC: O(1)
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        ans = []
        n, m=  len(land), len(land[0])
        def dfs(i,j, res):
            if i>=n or j>=m or i<0 or j<0 or land[i][j]== 0:
                return 
            
            res[2]= max(res[2], i)
            res[3]= max(res[3], j)
                
            land[i][j]= 0
            
            dfs(i+1, j,res)
            dfs(i, j+1,res)
            dfs(i-1, j,res)
            dfs(i, j-1,res)
        
        
        for i in range(n):
            for j in range(m):
                if land[i][j]==1:
                    res= [i,j,i,j]
                    dfs(i,j,res)
                    ans.append(res)
                    
        return ans
