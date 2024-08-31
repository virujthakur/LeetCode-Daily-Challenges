class Solution:
    #TC : (ELOGV) SC: O(N)
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = [[] for _ in range(n)]
        
        for i,e in enumerate(edges):
            u,v = e
            w = succProb[i]
            
            graph[u].append((w, v))
            graph[v].append((w, u))
            
        pq = []
        visited = set()
        distTo = [-1] * n
        
        heapq.heapify(pq)
        distTo[start_node] = 1
        heapq.heappush(pq, (-1, start_node))
        
        while pq:
            curProb, curNode = heapq.heappop(pq)
            curProb *= -1
            
            if curNode in visited:
                continue
                
            visited.add(curNode)
            if curNode == end_node:
                return curProb
            
            for nbr in graph[curNode]:
                if nbr[1] not in visited and distTo[nbr[1]] < curProb * nbr[0]:
                    distTo[nbr[1]] = curProb * nbr[0]
                    heapq.heappush(pq, (-distTo[nbr[1]], nbr[1]))
                    
        return 0
                    
                    
                    
