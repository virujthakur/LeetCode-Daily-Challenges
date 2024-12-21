class Solution:
    #TC: O(N) SC: O(N)
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        graph = [[] for _ in range(n)]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
          
        res =0
        visited= [False] * n
        def dfs(src):
            nonlocal res
            visited[src]= True
            
            s = values[src]
            for nbr in graph[src]:
                if not visited[nbr]:
                    s += dfs(nbr)
                 
            if s%k == 0:
                res +=1
                return 0
            
            return s
                    
        dfs(0)
        return res
                
            
            
