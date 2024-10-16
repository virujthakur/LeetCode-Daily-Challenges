class Solution:
    #TC : O(N) SC: O(1)
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        pq = []
        if a > 0:
            heapq.heappush(pq, (-a, "a"))
        if b > 0:
            heapq.heappush(pq, (-b, "b"))
        if c > 0:
            heapq.heappush(pq, (-c, "c"))
            
        ans = ''
        
        while len(pq) > 0:
            
            f= heapq.heappop(pq)
            # print(pq, f)
            
            if len(ans) < 2 or not (ans[-1] == f[1] and ans[-2] == f[1]):
                ans += f[1]
                if f[0] < -1:
                    heapq.heappush(pq, (f[0]+1, f[1]))
            else:
                if len(pq) == 0:
                    break
                
                s = heapq.heappop(pq)
                ans += s[1]
                
                if s[0] < -1:
                    heapq.heappush(pq, (s[0]+1, s[1]))
                
                heapq.heappush(pq, f)
                    
        return ans
            
