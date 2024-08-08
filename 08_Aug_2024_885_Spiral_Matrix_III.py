class Solution:
    #TC: O(4*N*M) SC: O(1)
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        di = [(0, 1), (1, 0), (0, -1) , (-1, 0)]
        
        visited= set()
        j = 0
        lenSpiral = 1
        
        answer = []
        curx = rStart
        cury = cStart
        answer.append((curx, cury))
        
        while (len(answer) < rows* cols):
            
            for i in range(lenSpiral):
                curx += di[j][0]
                cury += di[j][1]
                if curx < rows and curx >=0 and cury >=0 and cury < cols:
                    answer.append([curx, cury])
            
            j+=1
            
            if j%2 == 0:
                lenSpiral+=1
                
            j%=4
                
        return answer
            
