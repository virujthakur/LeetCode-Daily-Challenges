class Solution:
    #TC: O(N) SC: O(1)
    def countSubarrays(self, nums: List[int], k: int) -> int:
        mx = max(nums)
        n = len(nums)
        cnt = 0
        ans = 0
        i = 0
        for j in range(n):
            if nums[j] == mx:
                cnt +=1
            
            while i<=j and cnt ==k:
                ans += n-j
                if nums[i] == mx:
                    cnt-=1
                i+=1

        return ans
