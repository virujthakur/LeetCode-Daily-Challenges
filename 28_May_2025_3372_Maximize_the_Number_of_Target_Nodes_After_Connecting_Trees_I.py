class Solution:
    #TC: O(N^2 + O(M^2)) SC: O(N^2 + M^2)
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        def bfs_list(edges):
            f = defaultdict(list)
            sz= len(edges)+1
            graph = [[] for _ in range(sz)]
            for u,v in edges:
                graph[u].append(v)
                graph[v].append(u)
            
            for i in range(sz):
                q = deque()
                visited = [False] * sz
                ans = [0]* sz
                q.append(i)
                level = 0
                while q:
                    s = len(q)
                    ans[level] = s
                    for j in range(s):
                        cur = q.popleft()
                        visited[cur]= True
                        for nbr in graph[cur]:
                            if visited[nbr] == False:
                                q.append(nbr)

                    level+=1
                f[i] = ans

            return f

        f1 = bfs_list(edges1)
        f2 = bfs_list(edges2)

        n = len(edges1) +1
        m = len(edges2) +1

        for ke,v in f1.items():
            s = 0
            for i in range(n):
                s+= v[i]
                v[i] = s

            f1[ke] = v

        for ke,v in f2.items():
            s = 0
            for i in range(m):
                s+= v[i]
                v[i] = s

            f2[ke] = v

        ans = [0]* n
        ans2 = 0
        # print(f1)
        # print(f2)

        for i in range(n):
            if k>0:
                for(ke,v) in f2.items():
                    ans2 = max(ans2, v[min(m-1, k-1)])
            
            # print(f1[i][min(k, n-1)], ans2)
            ans[i]= f1[i][min(k, n-1)] + ans2 

        return ans
        

