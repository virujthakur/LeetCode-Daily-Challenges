class Solution:
    #TC: O(6!) SC:  O(6 * 6!)
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        '''
        up = idx -3
        down = idx + 3
        left = idx -1 on idx where (idx % 3 == 0) not possible to go left
        right = idx + 1 on idx where idx % 3 == 2 not possible to go right
        '''
        
        def get_new_configs(s):
            
            new_configs = []
            idx = s.find('0')
            
            if idx % 3 != 0:
                temp = list(s)
                temp[idx], temp[idx -1] = temp[idx - 1], temp[idx]
                new_configs.append(''.join(temp))
                
            if idx % 3 != 2:
                temp = list(s)
                temp[idx], temp[idx +1] = temp[idx + 1], temp[idx]
                new_configs.append(''.join(temp))
            
            if idx >=3:
                temp = list(s)
                temp[idx], temp[idx-3] = temp[idx-3], temp[idx]
                new_configs.append(''.join(temp))
                
            if idx < 3:
                temp = list(s)
                temp[idx], temp[idx+3] = temp[idx+3], temp[idx]
                new_configs.append(''.join(temp))
                
            return new_configs
        
        board_str = ''
        for i in range(2):
            for j in range(3):
                board_str += str(board[i][j])
                
        visited = defaultdict(bool)
        visited[board_str]= True
        q = deque()
        
        q.append(board_str)
        
        ans = 0
        while q:
            sz= len(q)
            
            for i in range(sz):
                x = q.popleft()
                if x == '123450':
                    return ans
                
                new_board_strs = get_new_configs(x)
                # print(new_board_strs)
                
                for nbr in new_board_strs:
                    if nbr == '123450':
                        return ans+1
                    
                    if visited[nbr]== False:
                        q.append(nbr)
                        visited[nbr]= True
                        
            ans+=1
            
        return -1
