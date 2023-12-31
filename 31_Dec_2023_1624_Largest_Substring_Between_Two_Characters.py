class Solution:
    #TC: O(N) SC: O(1)
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        n= len(s)
        
        fc = {}
        lc = {}
        for i in range (n):
            if s[i] not in fc:
                fc[s[i]]= i
            lc[s[i]]=i
        
        ans = -1
        for i in range(ord('a'), ord('z'AC)+1):
            if chr(i) in fc and chr(i) in lc:
                ans= max(ans, lc[chr(i)]- fc[chr(i)]-1)
                
        return ans
            
