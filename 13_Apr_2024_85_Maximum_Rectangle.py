class Solution:
    # TC: O(N*M*M) SC: O(M)
    def largestRectangleArea(self, heights: List[int]) -> int:
        n= len(heights)
        nse, pse = [n]*n, [-1]* n
        
        st= deque()
        for i in range(n):
            while st and heights[st[-1]] >= heights[i]:
                st.pop()
            
            if st:
                pse[i]= st[-1]
            
            st.append(i)
        
        st= deque()
        for i in range(n-1, -1, -1):
            while st and heights[st[-1]] >= heights[i]:
                st.pop()
            
            if st:
                nse[i]= st[-1]
            
            st.append(i)
        
        ans = 0
        for i in range(n):
            # print(heights[i]*  min(n,nse[i]- pse[i]-1))
            ans= max(ans, heights[i]*  min(n,nse[i]- pse[i]-1))
            
        return ans
    
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n, m= len(matrix), len(matrix[0])
        ans = 0
        histogram = [0]* m
        for i in range(n):
            for j in range(m):
                if matrix[i][j]== '1':
                    histogram[j]+=1
                else:
                    histogram[j] = 0
                
            ans = max(ans, self.largestRectangleArea(histogram))
            
        return ans
