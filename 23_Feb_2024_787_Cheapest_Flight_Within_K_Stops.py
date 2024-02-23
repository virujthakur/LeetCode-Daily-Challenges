import heapq
class Solution:
    #TC: O(N^2 (LOGN)) SC: O(N^2)
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        distTo = [10 ** 9] * n
        stopsTo= [10 ** 9] * n
        distTo[src], stopsTo[src] = 0, 0
        
        graph = [[] for _ in range(n)]
        for f, t, p in  flights:
            graph[f].append((p, t))
            
        pq= []
        heapq.heappush(pq,(0, 0, src))
        while pq:
            curCost, curLevel, curNode = pq[0]
            if curNode == dst:
                return curCost
            
            heapq.heappop(pq)
            if curLevel >= k+1:
                continue
            
            for nbrCost, nbrNode in graph[curNode]:
                if distTo[nbrNode] > curCost + nbrCost:
                    distTo[nbrNode]= curCost+ nbrCost
                    stopsTo[nbrNode]= curLevel + 1
                    heapq.heappush(pq, (distTo[nbrNode], curLevel+1, nbrNode))
                elif stopsTo[nbrNode] > curLevel + 1:
                    distTo[nbrNode]= curCost+ nbrCost
                    stopsTo[nbrNode]= curLevel + 1
                    heapq.heappush(pq, (distTo[nbrNode], curLevel +1 , nbrNode))
        
        return -1
        
        
