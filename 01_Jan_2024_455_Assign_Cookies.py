class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        #TC : O(NLOGN) SC: O(1)
        g.sort()
        s.sort()
        i=0
        j=0
        n= len(g)
        m= len(s)
        
        while(i< n and j< m):
            if s[j] >= g[i]:
                i+=1
            j+=1
            
        return i
