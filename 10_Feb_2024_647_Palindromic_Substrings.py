class Solution:
    #TC: O(N^2) SC: O(N^2)
    def countSubstrings(self, s: str) -> int:
        n= len(s)
        dp= [[-1]* n for _ in range(n)]
        def valid(i, j):
            if i>=j:
                return 1
            
            if dp[i][j]!= -1:
                return dp[i][j]
            
            if s[i]!= s[j]:
                dp[i][j]= 0
                return dp[i][j]
            
            dp[i][j]= valid(i+1, j-1)
            return dp[i][j]
        
        
        ans=0
        for i in range(n):
            for j in range(i, n):
                if valid(i,j):
                    ans+=1
                    
        return ans
            
