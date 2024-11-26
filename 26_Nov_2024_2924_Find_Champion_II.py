class Solution:
    #TC: O(Len(edges)) SC: O(N)
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indegree = [0] * n
        for u,v in edges:
            indegree[v]+=1
            
        champs = []
        for i in range(n):
            if indegree[i] == 0:
                champs.append(i)
                
        if len(champs) == 1:
            return champs[0]
        else:
            return -1
