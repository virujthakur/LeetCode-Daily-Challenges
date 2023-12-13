class Solution:
    
    # TC: O(N*M (N+M)) SC: O(1)
    def numSpecial(self, mat: List[List[int]]) -> int:
        m= len(mat)
        n= len(mat[0])
        ans = 0
        
        for i in range (m):
            for j in range (n):
                if mat[i][j] == 1:
                    flag= False
                    for k in range(m):
                        if i!=k and mat[k][j]==1 :
                            flag= True
                        
                    for k in range(n):
                        if j!=k and mat[i][k]==1 :
                            flag= True
                        
                    if not flag :
                        ans+=1
        return ans
                    
                        
        
