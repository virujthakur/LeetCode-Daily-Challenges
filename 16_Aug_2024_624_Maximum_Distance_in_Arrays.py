class Solution:
    #TC: O(M) SC: O(M)
    def maxDistance(self, arrays: List[List[int]]) -> int:
        m = len(arrays)
        
        suffixMax = [-10**9]* m
        suffixMin = [10**9] * m
        
        s_max, s_min = -10**9, 10**9
        for i in range(m-1, -1, -1):
            s_max = max(arrays[i][-1], s_max)
            s_min = min(arrays[i][0], s_min)
            suffixMax[i], suffixMin[i]= s_max, s_min
        
        ans = 0
        for i in range(m):
            if i+1 < m:
                poss1 = abs(arrays[i][0]- suffixMax[i+1])
                poss2 = abs(arrays[i][-1]- suffixMin[i+1])
                ans = max(ans, poss1, poss2)
                
        return ans
