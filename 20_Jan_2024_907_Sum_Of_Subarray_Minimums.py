#TC: O(N) SC: O(N)
from collections import deque
class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        mod = 10 ** 9 + 7
        n= len(arr)
        ans = 0
        s1,s2,s3,s4 = deque(), deque(), deque(), deque()
        nse= [n] * n
        pse= [-1] * n
        nses= [n] * n
        pses= [-1] * n
        
        for i in range (n-1, -1, -1):
            while s1 and arr[s1[-1]] >= arr[i]:
                s1.pop()
            if s1: 
                nse[i]= s1[-1]
            s1.append(i)
        
        for i in range (n-1, -1, -1):
            while s3 and arr[s3[-1]] > arr[i]:
                s3.pop()
            if s3: 
                nses[i]= s3[-1]

            s3.append(i)
            
            
        for i in range(n):
            while s2 and arr[s2[-1]] >= arr[i]:
                s2.pop()
            if s2: 
                pse[i]= s2[-1]

            s2.append(i)
            
        for i in range(n):
            while s4 and arr[s4[-1]] >= arr[i]:
                s4.pop()
            if s4: 
                pses[i]= s4[-1]

            s4.append(i)
        
        # print(nse, pse, nses, pses)
        vis = set()
        
        for i in range(n):
            
            ans+= (arr[i]* (nses[i]- i)) % mod
            ans+= (arr[i] * (i- pses[i])) % mod
            
            if i > 0 and i < n-1 :
                ans+= (arr[i]* ((nses[i]- i - 1) * (i- pses[i]-1)))% mod
                
        return (ans- sum(arr) + mod) % mod
        
       
            
