class Solution:
    #TC: O(NLOGN) SC: O(N)
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints= [t.split(':') for t in timePoints]
        for i,t in enumerate(timePoints):
            h,m = t
            timePoints[i]= (int(h), int(m))
            
        # timePoints.sort()
        
        n = len(timePoints)
        for i in range(n):
            h, m = timePoints[i]
            timePoints.append((h+ 24, m))
                
        timePoints.sort()
            
        ans= 10**9
        for i in range(1, len(timePoints)):
            h1, m1 = timePoints[i-1]
            h2, m2 = timePoints[i]
            
            ans= min(ans, (h2-h1)* 60 + m2-m1)
            
        return ans
