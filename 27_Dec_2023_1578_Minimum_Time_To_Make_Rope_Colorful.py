import heapq
class Solution:
    #TC: O(NLOGN) SC:O(N)
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n= len(colors)
        ans = 0
        h= []
        heapq.heapify(h)
        
        prevColor= ''
        for i in range(n):
            # print(h)
            if prevColor== colors[i]:
                heapq.heappush(h,neededTime[i])
                continue
            else:
                while len(h) > 1:
                    ans+= h[0]
                    heapq.heappop(h)
                
                while len(h) > 0:
                    heapq.heappop(h)
                prevColor= colors[i]
            
            heapq.heappush(h,neededTime[i])
        
        while len(h) > 1:
            ans+= h[0]
            heapq.heappop(h)
            
        return ans
                
            
