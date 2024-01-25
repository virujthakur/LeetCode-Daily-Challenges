class Solution:
    #TC: O(N*M) SC: O(N*M)
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        n, m= len(text1), len(text2)
        dp = [[-1] * m for _ in range(n)]
        
        def recur(i,j):
            if i==n or j==m:
                return 0
            
            if dp[i][j]!=-1:
                return dp[i][j]
            
            ans= 0
            if text1[i]== text2[j]:
                ans = 1+ recur(i+1, j+1)
            else:
                ans = max(recur(i+1, j+1), recur(i, j+1), recur(i+1, j))
                
            dp[i][j]= ans
            return dp[i][j]
        
        return recur(0, 0)
            
