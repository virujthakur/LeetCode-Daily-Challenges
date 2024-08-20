class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        
        #TC: O(N*N) SC: O(N*N)
        n = len(piles)
        @cache
        def recur(idx, m):
            if idx == n :
                return (0, 0)
            
            s = 0
            ansx = 0
            ansy = 0
        
            for i in range(idx, min(n, idx+ 2*m)):
                s += piles[i]
                y =  recur(i+1, max(m, i-idx + 1))
                           
                if s+ y[1] > ansx:
                    ansx = s+ y[1]
                    ansy = y[0]
                    
            return (ansx, ansy)
        
        return recur(0, 1)[0]
                
            
