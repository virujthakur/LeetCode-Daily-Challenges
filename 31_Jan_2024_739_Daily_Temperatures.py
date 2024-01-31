from collections import deque
class Solution:
    #TC : O(N) SC: O(N)
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        n= len(temps) 
        nge=[-1]*n
        ans= [0]*n
        
        st= deque()
        
        for i in range(n-1,-1,-1):
            while st and temps[st[-1]] <= temps[i]:
                st.pop()
            
            if st:
                nge[i]= st[-1]
            
            if nge[i]!= -1:
                ans[i]= nge[i]-i
            st.append(i)
        
