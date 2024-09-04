class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        #TC : O(N) SC: O(1)
        obs = [tuple(o) for o in obstacles]
        obs = set(obs)
        di = [(0,1), (1,0), (0,-1), (-1,0)]
        d = 0
        curx, cury = 0, 0
        ans = 0
        
        for c in commands:
            if c ==-2:
                d-=1
                if d < 0:
                    d += 4   
                d %= 4
                
            elif c== -1:
                d+=1
                d %= 4
                
            else:
                dx, dy = di[d]
                for i in range(c):
                    newx = curx + dx
                    newy = cury + dy
                    
                    if (newx, newy) in obs:
                        break
                    else:
                        curx= newx
                        cury= newy
                    
                # print(curx, cury)
                ans = max(ans, curx* curx + cury* cury)
                
        return ans
                
                
                    
                
                
