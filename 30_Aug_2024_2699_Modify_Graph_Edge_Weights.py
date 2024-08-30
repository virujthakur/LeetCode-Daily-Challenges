class Solution:
    #TC : E*E*LOG(V) SC : O(N)
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        m = len(edges)
        
        graph = [[] for _ in range(n)]
        
        for u,v,w in edges:
            if w !=-1:
                graph[u].append((w, v))
                graph[v].append((w, u))
                
        def djiktras(source, destination):
            distTo = [10**10] * n
            visited = [False] * n
            distTo[source] = 0
            pq = [(0, source)]
            heapq.heapify(pq)

            while pq:
                curCost, curNode = heapq.heappop(pq)

                if visited[curNode]:
                    continue

                for nbr in graph[curNode]:
                    if not visited[nbr[1]] and curCost + nbr[0] < distTo[nbr[1]]:
                        distTo[nbr[1]]= curCost + nbr[0]
                        heapq.heappush(pq, (distTo[nbr[1]], nbr[1]))
                        
            return distTo
                
        distTo = djiktras(source, destination)
            
        sd = distTo[destination]
        if sd < target:
            return []
        elif sd == target:
            for i, edge in enumerate(edges):
                u,v, w= edge
                if w < 0:
                    edges[i][2] = int(2e9)
                    
            
            return edges
        
        else:
            for i, edge in enumerate(edges):
                u,v, w = edge
                if w< 0:
                    graph[u].append((1,v))
                    graph[v].append((1,u))
                    
                    distTo = djiktras(source, destination)
                    sd = distTo[destination]
                    # print(sd)
                    
                    edges[i][2] = 1
                    
                    if sd <= target:
                        edges[i][2]+= target - sd

                        for j in range(i+1, m):
                            if edges[j][2] < 0:
                                edges[j][2] = int(2e9)


                        return edges
                
        return []
        
        
            
        
