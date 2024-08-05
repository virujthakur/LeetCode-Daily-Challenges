class Solution:
    #TC: O(N) SC: O(N)
    def kthDistinct(self, arr: List[str], k: int) -> str:
        f = defaultdict(int)
        for s in arr:
            f[s]+=1
        
        cnt = 0
        for s in arr:
            if f[s]==1:
                cnt+=1
                
            if cnt==k:
                return s
        
        return ""
        
