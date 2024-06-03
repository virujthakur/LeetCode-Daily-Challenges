class Solution:
    #TC: O(NLOGN) SC: O(1)
    def appendCharacters(self, s: str, t: str) -> int:
        n,m = len(s), len(t)
        f= defaultdict(list)
        for i,c in enumerate(s):
            f[c].append(i)
        
        prev = -1
        for j,c in enumerate(t):
            if len(f[c])> 0:
                r= bisect.bisect(f[c], prev, 0, len(f[c]))
                if r== len(f[c]):
                    return m- j
                
                prev= f[c][r]
            else:
                return m-j
                
        return 0
                
        
        
                
                
