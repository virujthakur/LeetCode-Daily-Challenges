class Solution:
    #TC : O(N*2) SC: O(1)
    def minimumDeletions(self, s: str) -> int:
        n= len(s)
        dp = [[-1]* 2 for _ in range(n)]
        
        def recur(idx, is_b_present):
            if idx==n:
                return 0
            
            if dp[idx][is_b_present]!= -1:
                return dp[idx][is_b_present]
            
            ans = 10**9
           
            ans = min(ans, 1+ recur(idx+1, is_b_present))
            
            if is_b_present and s[idx]!='a':
                ans = min(ans, recur(idx+1, is_b_present or s[idx]== 'b'))
            elif not is_b_present:
                ans = min(ans, recur(idx+1, is_b_present or s[idx]== 'b'))
             
            dp[idx][is_b_present]= ans
            return ans
        
        return recur(0, 0)
            
            
                
            
