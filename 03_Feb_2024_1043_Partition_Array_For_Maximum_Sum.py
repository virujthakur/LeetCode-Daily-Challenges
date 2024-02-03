class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        #TC: O(N*K) SC: O(N)
        n= len(arr)
        dp= [-1]*n
        def recur(i):
            if i==n: return 0
            
            if dp[i]!=-1:
                return dp[i]
            
            en= min(n,i+k)
            mx= 0
            ans= 0
            for j in range(i, en):
                mx= max(arr[j],mx)
                ans= max(ans, mx* (j-i+1)+ recur(j+1))
            
            dp[i]= ans
            return dp[i]
        
        return recur(0)
