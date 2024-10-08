class Solution:
    #TC: O(N) SC: O(1)
    def minSwaps(self, s: str) -> int:
        
        s= list(s)
        n = len(s)
        o,c = 0, 0
        op = n-1
        ans = 0
        
        for i in range(n):
            if s[i] == '[':
                o+=1
            else:
                c+=1
                
            if c > o:
                while op >=0 and s[op]!= '[':
                    op -=1
                
                s[i], s[op] = s[op], s[i]
                ans +=1
                c -=1
                o +=1
                
        return ans
                
                
            
