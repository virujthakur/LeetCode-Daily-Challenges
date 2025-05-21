class Solution:
    #TC: O(M*N*(M+N)) SC: O(1)
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m,n = len(matrix), len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    for k in range(n):
                        if matrix[i][k] != 0:
                            matrix[i][k] = -10**18

                    for k in range(m):
                        if matrix[k][j] != 0:
                            matrix[k][j] = -10**18

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == -10**18:
                    matrix[i][j] = 0

        
