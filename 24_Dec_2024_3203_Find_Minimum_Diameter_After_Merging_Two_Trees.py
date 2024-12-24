class Solution:
    #TC : O(N) SC :O(1)
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        n, m = len(edges1), len(edges2)
        graph1 = [[] for _ in range(n+1)]
        graph2 = [[] for _ in range(m+1)]
        
        for u,v in edges1:
            graph1[u].append(v)
            graph1[v].append(u)
            
        for u,v in edges2:
            graph2[u].append(v)
            graph2[v].append(u)
        
        def get_farthest_node(g):
            sz= len(g)
            q = deque()
            q.append(0)
            visited = [False]* sz
            
            last = -1
            
            while q:
                last= q.popleft()
                visited[last]= True
                for nbr in g[last]:
                    if not visited[nbr]:
                        q.append(nbr)
                        
            return last
        
        def get_diameter(g, last):
            q= deque()
            q.append(last)
            sz= len(g)
            visited = [False]* sz
            
            level = -1
            while q:
                level+=1
                sz = len(q)
                for i in range(sz):
                    cur = q.popleft()
                    visited[cur]= True
                    for nbr in g[cur]:
                        if not visited[nbr]:
                            q.append(nbr)
                
            return level
        
        l1 = get_farthest_node(graph1)
        # print(l1)
        d1 = get_diameter(graph1, l1)
        # print(d1)
        l2 = get_farthest_node(graph2)
        d2 = get_diameter(graph2, l2)
        # return 0
        
        r1= (d1+1)//2
        r2= (d2+1)//2
        
        return max(d1, d2, r1+r2+1)
                        
                        
