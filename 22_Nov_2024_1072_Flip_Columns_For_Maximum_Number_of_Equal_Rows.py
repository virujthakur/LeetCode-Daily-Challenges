class Solution:
    #TC: O(M*N) SC: O(2*M*N)
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        m,n = len(matrix), len(matrix[0])
        
        def inverse(s):
            inv = ''
            for i in range(len(s)):
                if s[i] == '0':
                    inv += '1'
                else:
                    inv += '0'
                    
            return inv
        
        ans = 0
        f = defaultdict(int)
        
        for i in range(m):
            row = ''
            for j in range(n):
                if matrix[i][j] == 0:
                    row += '0'
                else:
                    row += '1'
                    
            f[row]+=1
            # print(row, inverse(row))
            f[inverse(row)]+=1
                
        # print(f)
        for k,v in f.items():
            ans= max(ans, v)
            
        return ans
                    
                
