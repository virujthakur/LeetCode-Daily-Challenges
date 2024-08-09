class Solution:
    #TC: O(9*M*N) SC: O(1)
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        m, n = len(grid) , len(grid[0])
        
        def isValid(i, j):
            rowSum = [0]* 3
            colSum = [0]* 3
            d1, d2 = 0, 0
            visited = [False]* 9
            
            for x in range(i, i+3):
                for y in range(j, j+3):
                    if grid[x][y] > 9 or grid[x][y] == 0:
                        return False

                    visited[grid[x][y]-1]= True

                    rowSum[x- i]+= grid[x][y]
                    colSum[y- j]+= grid[x][y]

                    if x-i == y-j:
                        d1+= grid[x][y]

                    if x-i + (y-j) == 2:
                        d2+= grid[x][y]


            for v in visited:
                if not v:
                    return False

            if d1!= d2:
                return False

            for r in rowSum :
                if r != d1:
                    return False

            for c in colSum:
                if c != d1:
                    return False
                
            return True
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if i+3 <= m and j+3 <= n:
                    if isValid(i, j):
                        ans+=1
                        
        return ans
                        
                        
                            
                            
                            
