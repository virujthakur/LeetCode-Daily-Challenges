class Solution:
    #TC: O(N) SC: O(1)
    def minAddToMakeValid(self, s: str) -> int:
        cnt = 0
        ans = 0
        for c in s:
            if c== '(':
                cnt+=1
            else:
                cnt-=1
                
            if cnt < 0:
                cnt = 0
                ans+=1
                
        return ans + cnt if cnt > 0 else ans
