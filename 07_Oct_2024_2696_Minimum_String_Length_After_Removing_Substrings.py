class Solution:
    #TC: O(N^2) SC:O(1)
    def minLength(self, s: str) -> int:
        while "CD" in s or "AB" in s:
            s= s.replace("CD", '')
            s= s.replace("AB", '')
            
        return len(s)
            
