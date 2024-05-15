class Solution:
    #TC: O(N*N* LOG(N)) SC: O(N*N)
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        di = [(0,1), (0,-1), (1,0), (-1,0)]
        n= len(grid)
        
        # visited = [[False]* n for _ in range(n)]
        q= deque()
        for i in range(n):
            for j in range(n):
                if grid[i][j]== 1:
                    grid[i][j] = 0
                else:
                    grid[i][j]= 10**9
                
        for i in range(n):
            for j in range(n):
                if grid[i][j]== 0:
                    q.append((i,j))
                    
        while q:
            x,y= q.popleft()
            # print(f'visiting {x} , {y}')
            for d in di:
                newx= x+ d[0]
                newy= y+ d[1]
                
                if newx>=0 and newy>=0 and newx<n and newy<n and grid[newx][newy] > grid[x][y] + 1:
                        q.append((newx, newy))
                        grid[newx][newy]= min(grid[newx][newy],grid[x][y]+1)
                    
        
        # print(grid)
        
        
        pq= []
        pq.append([-grid[0][0],0,0])
        grid[0][0]=-1

        while pq:
            cur_safeness,x,y= heapq.heappop(pq)
            if x== n-1 and y== n-1:
                return -cur_safeness

            for d in di:
                newx = x+ d[0]
                newy = y+ d[1]

                if newx>=0 and newy>=0 and newx<n and newy<n and grid[newx][newy]!=-1:
                    heapq.heappush(pq, [-min(-cur_safeness, grid[newx][newy]), newx, newy])
                    grid[newx][newy] = -1
                    
            
        return -1
        
