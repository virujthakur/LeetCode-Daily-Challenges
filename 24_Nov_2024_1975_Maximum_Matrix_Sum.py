class Solution:
    #TC: O(N*N) SC: O(1)
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        
        s = 0
        mn = 10**9
        cnt = 0
        for i in range(n):
            for j in range(n):
                s += abs(matrix[i][j])
                mn = min(mn, abs(matrix[i][j]))
                
                if matrix[i][j] <=0:
                    cnt +=1
        
        if cnt %2 :
            return s  -2* mn
        else:
            return s
