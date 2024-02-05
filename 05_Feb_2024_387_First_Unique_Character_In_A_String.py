class Solution:
    #TC: O(N) SC: O(1)
    def firstUniqChar(self, s: str) -> int:
        n= len(s)
        f= defaultdict(list)
        for i,c in enumerate(s):
            f[c].append(i)
        
        ans= n
        for key,val in f.items():
            if len(val)==1:
                ans= min(ans,val[0])
                
        return ans if ans<n else -1
