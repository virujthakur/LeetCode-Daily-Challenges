class Solution:
    #TC: O(N) SC: O(1)
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        i = 0
        s = 0
        ans = 0
        for j in range(n):
            s += nums[j]
            while s * (j-i+1) >= k:
                s -= nums[i]
                i+=1

            ans+= j-i+1

        return ans
