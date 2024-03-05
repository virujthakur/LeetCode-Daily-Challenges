class Solution:
    #TC: O(N) SC: O(1)
    def minimumLength(self, s: str) -> int:
        n= len(s)
        i,j= 0,n-1
        while i<j:
            c1,c2= s[i], s[j]
            if c1 != c2:
                break
            
            while i<n and s[i]==c1:
                i+=1
            
            while j>=0 and s[j]==c1:
                j-=1
                
        return j-i+1 if j>=i else 0
