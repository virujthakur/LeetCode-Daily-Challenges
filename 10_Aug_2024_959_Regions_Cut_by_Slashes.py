class Solution:
    #TC: O(N*N) SC: O(N*N)
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        parent = [i for i in range((n+1)*(n+1))]
        rank =  [1] * (n+1)*(n+1)
        regions = 0
        
        def union(x, y):
            nonlocal regions
            px= find(x)
            py= find(y)
            
            if px!= py:
                if rank[px] < rank[py]:
                    parent[px]= py
                elif rank[px] > rank[py]:
                    parent[py] = px
                else:
                    parent[py] = px
                    rank[px]+=1
            else: 
                regions+=1
        
        def find(x):
            if parent[x] == x:
                return x
            parent[x] = find(parent[x])
            return parent[x]
        
        for i in range(n):
            union(i, i+1)
            
        for i in range(n* (n+1), n*(n+1)+ n):
            union(i, i+1)
            
        for i in range(0, (n*n+1) , n+1):
            union(i, i+n+1)
            
        for i in range(n, (n*n + n+ 1), n+1):
            union(i, i+n+1)
        
        for i in range(n):
            for j in range(n):
                if grid[i][j]== '/':
                    union((i+1) *(n+1) + j, i *(n+1) + j+ 1)
                elif grid[i][j] == '\\':
                    union(i *(n+1) + j, (i+1) *(n+1) + j+ 1)
                
        
        return regions
                    
                
