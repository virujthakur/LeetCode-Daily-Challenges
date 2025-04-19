class Solution:
    #TC: O(NLOGN) SC: O(1)
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        nums.sort()
        # print(nums)
        ans = 0
        for i in range(n):
            j1= bisect.bisect_left(nums, lower- nums[i], i+1, n)
            j2= bisect.bisect_right(nums, upper - nums[i] , i+1, n)
            # print(j1, j2)
            ans+= j2- j1
            
        return ans
