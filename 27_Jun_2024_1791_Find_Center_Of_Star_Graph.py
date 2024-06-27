class Solution:
    #TC: O(N) SC: O(N)
    def findCenter(self, edges: List[List[int]]) -> int:
        n= len(edges)
        indegree =[0] * (n+1)
        for u,v in edges:
            indegree[u-1]+=1
            indegree[v-1]+=1
        
        for i in range(n+1):
            if indegree[i]== n:
                return i+1
            
        return -1
        
