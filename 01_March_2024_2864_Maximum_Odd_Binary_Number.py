class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        s= sorted(s, reverse= True)
        i= len(s)-1
        while i>=0 and s[-1]!=1:
            if s[i]=='1':
                s[i], s[-1]= s[-1], s[i]
            i-=1
        
        return ''.join(s)
