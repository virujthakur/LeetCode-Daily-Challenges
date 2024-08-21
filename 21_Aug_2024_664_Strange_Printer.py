class Solution:
    #TC: O(N*N*N) SC: O(N*N)
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        
        @cache
        def recur(i, j):
            if i==j:
                return 1
            if i>j:
                return 0
            
            ans = 1+ recur(i+1, j)
            for k in range(i+1, j+1):
                if s[i]== s[k]:
                    ans = min(ans, recur(i, k-1) + recur(k+1, j))
                    
            return ans
        
        return recur(0, len(s)-1)
         
