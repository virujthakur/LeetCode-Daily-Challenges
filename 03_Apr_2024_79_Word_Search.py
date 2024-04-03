class Solution:
    # TC: EXPONENTIAL SC: O(1)
    def exist(self, board: List[List[str]], word: str) -> bool:
        n= len(board)
        m= len(board[0])
        di = [[0,1], [0,-1], [1,0], [-1, 0]]
        ans= False
        
        def dfs(x, y, visited, nextIdx):
            nonlocal ans
            # print(board[x][y])
            if nextIdx == len(word):
                ans= True
                return
            
            # visited[x][y]= 1
            
            for d in di:
                newx= x+ d[0]
                newy= y+ d[1]
                if newx < n and newy < m and newx>=0 and newy>=0:
                    if visited[newx][newy]== 1:
                        continue
                    if board[newx][newy] == word[nextIdx]:
                        # visited[newx][newy]=1
                        newvisited= [row[:] for row in visited]
                        newvisited[newx][newy]=1
                        dfs(newx, newy, newvisited , nextIdx+1)
                        
        for i in range(n):
            for j in range(m):
                if board[i][j]== word[0]:
                    vis = [[-1 for __ in range(m)] for _ in range(n)]
                    vis[i][j]= 1
                    dfs(i, j, vis, 1)
                    
        return ans
