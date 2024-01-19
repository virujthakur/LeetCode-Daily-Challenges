class Solution:
    #TC: O(N^2) SC: O(1)
    def minFallingPathSum(self, mat: List[List[int]]) -> int:
        n= len(mat)
        dp= [[-1]*n for _ in range(n)] 
        
        for i in range(n):
            dp[n-1][i]= mat[n-1][i]
        
        for i in range(n-2, -1, -1):
            for j in range(n):
                dp[i][j]= mat[i][j]+ min(dp[i+1][j], dp[i+1][j+1] if j+1 < n else 10**9 , dp[i+1][j-1] if j-1>=0 else 10**9) 
       
        # print(dp)
        return min(dp[0])
