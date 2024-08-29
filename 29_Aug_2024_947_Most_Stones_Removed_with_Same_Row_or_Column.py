class Solution:
    #TC : O(N^2) SC: O(N)
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        parent = [_ for _ in range(n)]
        rank = [1] * n
        
        def find(x):
            if x==parent[x]:
                return x
            
            parent[x] = find(parent[x])
            return parent[x]
            
        def union(x, y):
            px = find(x)
            py = find(y)
            
            if px != py:
                if rank[px] > rank[py]:
                    parent[py]= px
                elif rank[py] > rank[px]:
                    parent[px] = py
                else:
                    parent[py]= px
                    rank[px]+=1
                    
        
        for i in range(n):
            for j in range(i+1, n):
                x1, y1 = stones[i]
                x2, y2 = stones[j]
                
                if x1== x2 or y1== y2:
                    union(i, j)
                    
        components = 0
        for i in range(n):
            if parent[i]== i:
                components+=1
                
        return n- components
        
        
