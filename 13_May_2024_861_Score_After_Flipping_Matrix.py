class Solution:
    #TC: O(M*N) SC: O(1)
    def matrixScore(self, grid: List[List[int]]) -> int:
        m= len(grid)
        n= len(grid[0])
        ans = 0
        
        def get_score():
            score = 0
            for i in range(m):
                val = 0
                for j in range(n):
                    val = (val<<1) | grid[i][j]
                # print(int(b,2))
                score+= val
                
            return score
        
        def flip_row(row):
            for j in range(n):
                grid[row][j] ^= 1
                
        def flip_column(column):
            for i in range(m):
                grid[i][column] ^= 1
        
        for i in range(m):
            if grid[i][0]== 0:
                flip_row(i)
                
        for j in range(n):
            cnt0 = 0
            for i in range(m):
                if grid[i][j]== 0:
                    cnt0 +=1
                    
            cnt1 = m - cnt0
            if cnt0 > cnt1:
                flip_column(j)
                
        return get_score()
            
