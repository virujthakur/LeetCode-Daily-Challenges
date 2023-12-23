class Solution:
    def isPathCrossing(self, path: str) -> bool:
        n= len(path)
        s= set()
        s.add((0,0))
        curX= curY= 0
        
        for c in path:
            if(c== 'N'):
                curY-=1
            elif(c== 'S'):
                curY+=1
            elif(c=='E'):
                curX+=1
            else:
                curX-=1
            
            if (curX, curY) in s:
                return True
            s.add((curX,curY))
        
        return False
            
        
