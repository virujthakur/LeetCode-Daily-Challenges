class Solution:
    #TC: O(N+M) SC: O(N+ M)
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        n = len(edges1)+1
        m = len(edges2)+1
        
        def compute(graph):
            cnt_even = [0] * len(graph)
            cnt_odd = [0] * len(graph)
            visited = [False] * len(graph)

            def dfs(r):
                visited[r]= True
                o, e = 0,0
                for nbr in graph[r]:
                    if visited[nbr]== False:
                        o1, e1 = dfs(nbr)
                        o+= e1
                        e+= o1

                e+=1
                cnt_odd[r] = o
                cnt_even[r] = e
                return o,e

            dfs(0)
            # print(cnt_even, cnt_odd)

            visited = [False] * len(graph)
            
            def dfs2(r, par):
                visited[r]= True

                for nbr in graph[r]:
                    if visited[nbr]== False:
                        cnt_odd[nbr] += cnt_even[r]- cnt_odd[nbr]
                        cnt_even[nbr] += cnt_odd[r]- cnt_even[nbr]
                        dfs2(nbr, r)

            dfs2(0, -1)
            
            return cnt_even,cnt_odd
            
        graph1 = [[] for _ in range(n)]
        graph2 = [[] for _ in range(m)]

        for u,v in edges1:
            graph1[u].append(v)
            graph1[v].append(u)

        for u,v in edges2:
            graph2[u].append(v)
            graph2[v].append(u)

        cnt_even_1, cnt_odd_1 = compute(graph1)
        cnt_even_2, cnt_odd_2 = compute(graph2)

        ans = [0] * n
        mx_odd = max(cnt_odd_2)
        for i in range(n):
            ans[i] = cnt_even_1[i] + mx_odd

        return ans
