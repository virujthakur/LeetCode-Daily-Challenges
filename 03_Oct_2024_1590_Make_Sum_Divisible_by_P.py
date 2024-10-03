class Solution:
    #TC: O(N) SC: O(P)
    def minSubarray(self, nums: List[int], p: int) -> int:
        n= len(nums)
        s= sum(nums)
        rem = s% p
        if rem == 0:
            return 0
        mp = {0: -1}
        
        cur = 0
        ans = n
        for i in range(n):
            cur += nums[i]
            cur %= p
            
            reqd = (cur - rem + p) % p
            if reqd in mp:
                ans = min(ans, i- mp[reqd])
                
            mp[cur] = i
                
        return ans if ans < n else -1
            
            
