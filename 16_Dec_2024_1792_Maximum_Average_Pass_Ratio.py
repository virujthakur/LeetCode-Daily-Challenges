class Solution:
    '''
    x/y
    (x+1) / (y+1)
    
    x+1 / y+1 - x/y
    '''
    #TC: O(NLOGN) SC: O(N)
    def calcDelta(self, x,y):
        return ((x+1)/ (y+1)) - (x/y)
    
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        myClasses = [[-self.calcDelta(c[0],c[1]) ,c[0], c[1]] for c in classes]
        minHeap = heapq.heapify(myClasses)
        
        while(extraStudents > 0):
            x = heapq.heappop(myClasses)
            x[1], x[2] = x[1]+1, x[2]+1
            x[0] = -self.calcDelta(x[1],x[2])
            heapq.heappush(myClasses, x)
            extraStudents -=1
            
        ans = 0.0
        while myClasses:
            x = heapq.heappop(myClasses)
            ans += x[1]/ x[2]
            
        return ans/ len(classes)
            
            
        
                
