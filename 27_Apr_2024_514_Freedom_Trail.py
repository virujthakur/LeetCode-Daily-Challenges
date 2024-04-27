class Solution:
    #TC: O(N^3) SC: O(N^2)
    def findRotateSteps(self, ring: str, key: str) -> int:
        n= len(ring)
        dp= [[-1]* len(key) for _ in range(n)]
        
        def recur(i, j):
            if j== len(key):
                return 0
            
            # print(i,j)
            if dp[i][j]!=-1:
                return dp[i][j]
            
            ans = 10** 9
                
            for k in range(n):
                if ring[(i+k)% n]== key[j]:
                    ans= min(ans, k+1+ recur((i+k)%n, j+1))
                    
            for k in range(n):
                if ring[(i-k+n)% n]== key[j]:
                    ans= min(ans, k+1+ recur((i-k+n)%n, j+1))
                    
            dp[i][j]= ans
            return dp[i][j]
        
        return recur(0, 0)
                    
                
