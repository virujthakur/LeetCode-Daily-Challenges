class Solution:
    #TC: O(2^N) SC: O(N)
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)
        ans = 0
        visited = set()
        
        def recur(idx):
            nonlocal ans
            nonlocal visited
            if idx >=n:
                ans = max(ans, len(visited))
                return
            
            for j in range(idx, n):
                if s[idx: j+1] not in visited:
                    visited.add(s[idx: j+1])
                    recur(j+1)
                    visited.remove(s[idx: j+1])
                
        recur(0)
        return ans
            
            
            
