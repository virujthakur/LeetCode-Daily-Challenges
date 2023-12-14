class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        #TC: O(M* N) SC: O(M*N + 2*M + 2*N)
        m= len(grid)
        n= len(grid[0])
        onesRow=[0] * m
        onesCol=[0] * n
        zeroesRow=[0] * m
        zeroesCol=[0] * n
        
        for i in range (m):
            for j in range (n):
                if grid[i][j] == 1:
                    onesRow[i]+=1
                    onesCol[j]+=1
                else:
                    zeroesRow[i]+=1
                    zeroesCol[j]+=1
                    
        diff = [[0]* n for i in range (m)]
        
        for i in range (m):
            for j in range (n):
                diff[i][j]= onesRow[i]+ onesCol[j]- zeroesRow[i]- zeroesCol[j]
                
        return diff
