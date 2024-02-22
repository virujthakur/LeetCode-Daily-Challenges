class Solution:
    # TC: O(len(trust)) SC: O(N)
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n==1:
            return 1
        if not trust:
            return -1
            
        indegree= [0]* n
        outdegree= [0] * n
        for u,v in trust:
            indegree[v-1] +=1
            outdegree[u-1] += 1
            
        for i in range(n):
            if outdegree[i]== 0 and indegree[i] == n-1:
                return i+1
            
        return -1
            
