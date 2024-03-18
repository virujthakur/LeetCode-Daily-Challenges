class Solution:
    #TC: O(N(LOG(N))) SC: O(N)
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        n= len(points)
        ans= []
        
        i=0
        while i < n:
            j= i+1
            x1, y1= points[i]
            while j < n:
                x2, y2= points[j]
                if x2 <= y1:
                    x1= max(x1, x2)
                    y1= min(y1, y2)
                    j+=1
                else:
                    break
                
            # print(i, j)
            
            i= j
            ans.append([x1, y1])
         
        # print(ans)
        return len(ans)
                    
                
