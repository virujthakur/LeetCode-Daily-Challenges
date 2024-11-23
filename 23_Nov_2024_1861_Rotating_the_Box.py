class Solution:
    #TC: O(M*N) SC: O(M*N)
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m,n = len(box), len(box[0])
        
        for i in range(m):
            lastPos = n
            for j in range(n-1,-1, -1):
                if box[i][j] == '.':
                    continue
                elif box[i][j] == '*':
                    lastPos = j
                else:
                    val = box[i][j]
                    box[i][j] = '.'
                    box[i][lastPos - 1] = val
                    lastPos -=1
                    
        ans = [['.']* m for _ in range(n)]
        for j in range(n):
            for i in range(m):
                ans[j][m-1-i] = box[i][j]
        
        return ans
                    
                
