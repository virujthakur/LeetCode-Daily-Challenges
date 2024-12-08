class Solution:
    #TC: O(2*N*LOGN) SC: O(2*N)
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        n= len(events)
        
        dp = [[-1]* 3 for _ in range(n)]
        
        def recur(idx, cnt):
            if cnt == 2:
                return 0
            
            if idx == n:
                return 0
            
            if dp[idx][cnt]!=-1:
                return dp[idx][cnt]
            
            ans = 0
            ans = max(ans, recur(idx+1, cnt))
            
            j = bisect.bisect_left(events, [events[idx][1]+1, -1], idx, n)
                    
            ans = max(ans, events[idx][2] + recur(j, cnt+1))
            
            dp[idx][cnt]= ans
            return ans
        
        return recur(0, 0)
