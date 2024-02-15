class Solution:
    #TC: O(N) SC: O(1)
    def largestPerimeter(self, nums: List[int]) -> int:
        ans = 0
        nums.sort()
        n = len(nums)
        s = 0
        for i in range(n):
            if i > 1  and s > nums[i]:
                ans = max(ans, s+ nums[i])
            s+= nums[i]
        return ans if ans > 0 else -1
            
