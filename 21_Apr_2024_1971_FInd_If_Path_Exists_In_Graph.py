class Solution:
    #TC: O(N) SC: O(N)
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph= [[] for _ in range(n)]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
            
        visited= [False]* n
        ans= False
        
        def dfs(src):
            nonlocal ans
            if src== destination:
                ans= True
                return
            
            visited[src]= True
            
            for nbr in graph[src]:
                if not visited[nbr]:
                    dfs(nbr)
                    
        
        dfs(source)
        return ans
