class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        #TC: O(N*2N) SC: O(N*N)
        graph =[[] for _ in range(n)]
        
        for i in range(n-1):
            graph[i].append(i+1)
            
        def bfs():
            q= deque()
            q.append(0)
            visited = [False] * n
            
            ans = 0
            while(q):
                sz = len(q)
                for i in range(sz):
                    x = q.popleft()
                    visited[x]= True
                    
                    if x == n-1:
                        return ans
                    
                    for nbr in graph[x]:
                        if visited[nbr]== False:
                            q.append(nbr)
                            
                ans+=1
                
            return -1
                            
            
        ans = []
        for u,v in queries:
            graph[u].append(v)
            
            ans.append(bfs())
            
        return ans
            
