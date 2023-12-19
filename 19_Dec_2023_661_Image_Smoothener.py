class Solution:
    #TC: O(M*N) SC: O(N* M)
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m = len(img)
        n = len(img[0])
        ans= [[-1]* n for i in range (m)]
        
        for i in range (m):
            for j in range (n):
                avg = 0
                s= 0
                cnt= 0
                for wini in range(-1,2):
                    for winj in range (-1,2):
                        if (i+ wini) < m and (i + wini) >=0 and (j+winj) < n and (j+winj) >=0:
                            s+= img[i+wini][j+winj]
                            cnt+= 1
                
                # print(i,j,s,cnt)
                ans[i][j]= int(s/cnt)
        
        return ans
        
