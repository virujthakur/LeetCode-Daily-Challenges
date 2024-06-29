class Solution:
    #TC: N^2*LOGN SC: O(N)
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph= [[] for _ in range(n)]
        indegree= [0]* n
        
        for u,v in edges:
            indegree[v]+=1
            graph[u].append(v)
            
        q= deque()
        for i in range(n):
            if indegree[i]==0:
                q.append(i)
                
        ans= [set() for _ in range(n)]
                
        while q:
            cur= q.popleft()
            for nbr in graph[cur]:
                indegree[nbr]-=1
                for node in ans[cur]:
                    ans[nbr].add(node)
                ans[nbr].add(cur)
                if indegree[nbr]== 0:
                    q.append(nbr)
                    
        for i,a in enumerate(ans):
            ans[i]= list(ans[i])
            ans[i].sort()
            
            
        return ans
            
