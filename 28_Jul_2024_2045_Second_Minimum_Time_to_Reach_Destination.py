class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        #TC: N^2 LOGN SC: O(N^2)
        graph = [[] for _ in range(n+1)]
        
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        visited = [0]* (n+1)
        dist1 = [10**9] * (n+1)
        dist2 = [10**9] * (n+1)
        
        dist1[1] = 0
        
        pq = [(0, 1)]
        
        while pq:
            curCost, cur = heapq.heappop(pq)
            visited[cur] += 1
            
            if visited[cur] == 2 and cur == n:
                return curCost
            
            signal = curCost // (change)
            
            if signal % 2 == 1:
                curCost = (signal+1 )* change
            
            for nbr in graph[cur]:
                if visited[nbr] < 2:
                    newCost = curCost + time
                    if dist1[nbr] > newCost:
                        dist2[nbr]= dist1[nbr]
                        dist1[nbr]= newCost
                        heapq.heappush(pq, (newCost, nbr))
                        
                    elif dist2[nbr] > newCost and dist1[nbr]!= newCost:
                        dist2[nbr]= newCost
                        heapq.heappush(pq, (newCost, nbr))
        
        return -1
                    
            
            
