class Solution(object):
    def transpose(self, matrix):
        """
        TC: O(N*M) SC: O(N*M)
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        
        n = len(matrix)
        m = len(matrix[0])
        
        t= [[-1]* n for i in range(m)]
        # print(len(t))
        # print(len(t[0]))
        # print (t)
        
        for i in range (n) :
            for j in range (m) :
                t[j][i]= matrix[i][j]
                
        return t
        
        
