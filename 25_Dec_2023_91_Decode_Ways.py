class Solution:
    def numDecodings(self, s: str) -> int:
        #TC: O(N*N) SC: O(N)
        mp={}
        n= len(s)
        for i in range (ord('A'), ord('Z')+ 1):
            mp[str(i- ord('A')+1)] = chr(i)
        
        dp= [-1]* n
        
        def recur(idx):
            if idx == n:
                return 1
            
            if dp[idx] != -1:
                return dp[idx]
            
            ans= 0
            for i in range(idx, n):
                temp = s[idx:i+1]
                if temp in mp:
                    ans+= recur(i+1)
                  
            dp[idx]= ans
            return dp[idx]
        
        return recur(0)
        
