class Solution:
    def minSteps(self, n: int) -> int:
        #TC: O(N^2) SC: O(1)
        dp = [[-1]* (n+1) for _ in range(n+1)]
        
        def recur(idx, prev):
            # print(idx, prev)
            if idx == n:
                return 0
            
            if idx > n:
                return 10**9
            
            if dp[idx][prev]!=-1:
                return dp[idx][prev]
            
            ans = 10**9
            ans = min(ans, 1+ recur(idx+ prev, prev)) #paste operation
            
            if prev != idx:
                ans = min(ans, 1+ recur(idx, idx)) #copy operation
            
            # print(idx, prev, ans)
            dp[idx][prev]= ans
            return ans
        
        if n==1:
            return 0
        return 1+ recur(1, 1)
