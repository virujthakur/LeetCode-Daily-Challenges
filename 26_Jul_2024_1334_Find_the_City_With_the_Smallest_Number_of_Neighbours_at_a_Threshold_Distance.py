class Solution:
    #TC: O(N^3) SC: O(N^2)
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        distTo= [[10**9]* n for _ in range(n)]
        for u,v,w in edges:
            distTo[u][v] = w
            distTo[v][u] = w
            
        for i in range(n):
            distTo[i][i]= 0
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    distTo[i][j]= min(distTo[i][j], distTo[i][k]+ distTo[k][j])
                    
        # print(distTo)
        
        ans = -1
        ansCnt = 10**9
        for i in range(n):
            cnt = 0
            for j in range(n):
                if j== i:
                    continue
                if distTo[i][j] <= distanceThreshold:
                    cnt+=1
            
            # print(i, cnt)
            if cnt <= ansCnt:
                ansCnt = cnt
                ans = i
                
        return ans
            
