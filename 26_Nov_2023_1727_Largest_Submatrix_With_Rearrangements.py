class Solution:
    #TC: O(N*M) SC: O(N)
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m= len(matrix)
        n= len(matrix[0])
        res= 0
        ones_in_column = [0]* n
    
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0 :
                    ones_in_column[j] = 0
                else :
                    ones_in_column[j] +=1
            
            cur = sorted(ones_in_column, reverse= True)
            
            for j in range(n):
                res= max(res, (j+1)* cur[j])
            
        return res
