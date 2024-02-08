class Solution:
    def numSquares(self, n: int) -> int:
        
        #TC: O(N* sqrt(N)) SC: O(N)
        ans= 10** 9
        lim= n
        dp = [10** 9] * (n+1)
        
        dp[1], dp[0] = 1, 0
        
        for i in range(n+1):
            for j in range(int(sqrt(i))+ 1):
                dp[i]= min(dp[i], dp[i- j*j]+ 1)
                
        
        return dp[n]
                
