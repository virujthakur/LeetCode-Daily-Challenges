class Solution:
    #TC: O(M*N * (LOG (M*N)) SC: O(M*N)
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        directions= [(0,1), (1,0), (0,-1) , (-1,0)]
        distTo = [[10**9] * n for _ in range(m)]
        distTo[0][0] = 0
        
        pq = [(grid[0][0],0,0)]
        
        while pq:
            curCost, x, y = heapq.heappop(pq)
            grid[x][y]= -1
            
            if x== m-1 and y== n-1:
                return curCost
            
            for dx, dy in directions:
                newx = x + dx
                newy = y + dy
                
                if 0 <= newx < m and 0 <= newy < n and grid[newx][newy]!=-1:
                    if distTo[newx][newy] > distTo[x][y]+ grid[newx][newy]:
                        distTo[newx][newy] = distTo[x][y] + grid[newx][newy]
                        heapq.heappush(pq, (distTo[newx][newy], newx, newy))
                        
        return -1
                
                
