class Solution:
    #TC: O(N* Target) SC: O(N* Target)
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        
        mod = 10 ** 9 + 7
        dp= [[-1]* (target+1) for i in range (n)]
        # print(dp)
        def recur(i, s):
            
            if s > target:
                return 0
            
            if i == n:
                return s== target
            
            if dp[i][s]!= -1:
                return dp[i][s]
            
            ways = 0
            for j in range(1, k+1):
                ways+= (recur(i+1, s+ j) % mod)
            
            dp[i][s]= ways % mod
            return ways % mod
        
        return recur(0, 0)% mod
        
