class Solution:
    #TC: O(N*M) SC: O(N*M)
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0]* (n+1) for _ in range(m+1)]
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                
                if matrix[i][j]== 1:
                    dp[i][j] = min(dp[i+1][j+1], dp[i][j+1], dp[i+1][j])
                    if matrix[i][j]==1:
                        dp[i][j]+=1
         
        ans = 0
        for i in range(m):
            for j in range(n):
                ans += dp[i][j]
             
        # print(dp)
        return ans
                
