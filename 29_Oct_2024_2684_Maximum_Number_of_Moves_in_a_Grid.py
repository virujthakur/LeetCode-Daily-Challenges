class Solution:
    #TC: O(N*M) SC: O(N*M)
    def maxMoves(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        @cache
        def recur(row, col):
            if col == m:
                return 0
            
            ans1, ans2, ans3 = 0, 0, 0
            if row-1 >=0 and col+1 < m and grid[row-1][col+1] > grid[row][col]:
                ans1 = 1+ recur(row-1, col+1)
                
            if row+1 < n and col+1 < m and grid[row+1][col+1] > grid[row][col]:
                ans2 = 1+ recur(row+1, col+1)
            
            if col+1 < m and grid[row][col+1] > grid[row][col]:
                ans3 = 1+ recur(row, col+1)
            
            return max(ans1, ans2, ans3)
        
        ans = 0
        for i in range(n):
            ans = max(ans, recur(i, 0))
            
        return ans
            
            
