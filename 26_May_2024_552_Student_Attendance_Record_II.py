class Solution:
    def checkRecord(self, n: int) -> int:
        #TC: O(N*2*2) SC: O(N*2*2)
        dp = [[[-1]* 2 for _ in range(2)] for __ in range(n)]
        mod = 10**9+ 7
        def recur(idx, absent_count, flag):
            if idx > n:
                return 0
            
            if absent_count< 0:
                return 0
            
            if idx== n:
                return 1
            
            if dp[idx][absent_count][flag]!=-1:
                return dp[idx][absent_count][flag]
            
            ans = 0
            ans += recur(idx+1, absent_count-1, True) #student was absent
            ans%= mod
            ans += recur(idx+1, absent_count, True) #student was present
            ans%= mod
                
            if flag:
                for i in range(1, 3): #student was late
                    ans+= recur(idx+i, absent_count, False)
                    ans%= mod
             
            dp[idx][absent_count][flag]= ans% mod
            return ans
        
        return recur(0, 1, 1)
                
            
        
