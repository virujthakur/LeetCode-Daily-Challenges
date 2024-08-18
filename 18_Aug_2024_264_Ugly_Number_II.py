class Solution:
    def nthUglyNumber(self, n: int) -> int:
        #TC: O(NLOGN) SC: O(1)
        num = 0
        
        minheap = [1,]
        visited = set()
        
        while len(visited) < n:
            x = heapq.heappop(minheap)
            if x in visited:
                continue
                
            visited.add(x)
            
            for mul in [2,3,5]:
                if x*mul not in visited:
                    heapq.heappush(minheap, x* mul)
        
        return sorted(list(visited))[-1]
