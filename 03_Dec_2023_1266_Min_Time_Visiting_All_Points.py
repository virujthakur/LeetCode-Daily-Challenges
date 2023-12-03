class Solution:
    # TC: O(N) SC: O(1)
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans=0;
        n= len(points)
        
        for i in range (1, n):
            x1, y1= points[i]
            x2, y2= points[i-1]
            d= min(abs(x1-x2), abs(y1-y2))
            
            if abs(x1-x2)== d:
                ans+= abs(y2-y1)
            else :
                ans+= abs(x2-x1)
                
        return ans    
