class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        n, m = len(matrix), len(matrix[0])
        #TC: O(M*M*N) SC: O(N*M)
        
        prefixSum= [[0]* m for i in range(n)]
            
        for i in range(0, n):
            prefixSum[i][0]= matrix[i][0]
            for j in range(1, m):
                prefixSum[i][j]= matrix[i][j]+ prefixSum[i][j-1]
        
        ans = 0
        for y1 in range(m):
            for y2 in range(y1, m):
                f= defaultdict(int)
                f[0]= 1
                s = 0
                
                for i in range(n):
                    s+= (prefixSum[i][y2]- prefixSum[i][y1-1]) if y1-1>=0 else prefixSum[i][y2]
                    ans += f[s- target]
                    f[s]+= 1
                    
        return ans
