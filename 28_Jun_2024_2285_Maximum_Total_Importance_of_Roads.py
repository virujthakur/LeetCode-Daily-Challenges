class Solution:
    #TC: O(NLOGN) SC: O(N)
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        indegree= [0]* n
        graph = [[] for _ in range(n)]
        for u,v in roads:
            graph[u].append(v)
            graph[v].append(u)
            indegree[u]+=1
            indegree[v]+=1
            
        rank= [0]* n
        
        indegree_and_node = []
        for i in range(n):
            indegree_and_node.append((indegree[i], i))
            
        indegree_and_node.sort()
        for i in range(n):
            rank[indegree_and_node[i][1]] = i+1
            
        # print(rank)
            
        ans = 0
        for u,v in roads:
            ans+= rank[u]+ rank[v]
            
        return ans
            
            
        
