class Solution:
    # TC: O(N* 3) SC: O(N* 3)
    def numberOfWays(self, corridor: str) -> int:
        n= len(corridor)
        mod = 10 ** 9 + 7
        dp = [[-1,-1, -1] for i in range(n)] 
        
        def recur(i, seats):
            
            # print(f'{i} {seats}')
            
            if i == n and seats == 2 :
                return 1
            
            if i == n :
                return 0
            
            if dp[i][seats] != -1 :
                return dp[i][seats]
            
            ways = 0
            if corridor[i]== 'S' :
                seats+=1
                if seats == 2:
                    ways+= recur(i+1, 0) % mod
                    ways+= recur(i+1, seats) % mod
                
                elif seats < 2:
                    ways= recur(i+1, seats) % mod
                else:
                    return 0
                    
            else :
                if seats == 2:
                    ways+= recur(i+1, 0) % mod
                    ways+= recur(i+1, 2) % mod
                
                elif seats < 2:
                    ways= recur(i+1, seats) % mod
            
            dp[i][seats]= ways % mod
            return ways % mod
        
        return recur(0, 0) % mod   
