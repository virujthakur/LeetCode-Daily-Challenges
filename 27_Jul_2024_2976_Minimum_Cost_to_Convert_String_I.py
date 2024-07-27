class Solution:
    #TC: O(26*26*26 + O(N)) SC: O(26*26)
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        
        distTo= [[10**9]* 26 for _ in range(26)]
        for i in range(26):
            distTo[i][i]= 0
            
        n= len(original)
        for i in range(n):
            u = ord(original[i])- ord('a')
            v = ord(changed[i])- ord('a')
            distTo[u][v]= min(distTo[u][v], cost[i])
            
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    distTo[i][j]= min(distTo[i][j], distTo[i][k]+ distTo[k][j])
                    
        
        ans = 0
        m = len(source)
        for i in range(m):
            u = ord(source[i])- ord('a')
            v = ord(target[i])- ord('a')
            if distTo[u][v] == 10**9:
                return -1
            
            ans+= distTo[u][v]
            
        return ans
            
