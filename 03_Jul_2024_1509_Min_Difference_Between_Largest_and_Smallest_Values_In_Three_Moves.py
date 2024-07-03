class Solution:
    #TC: O(NLOGN) SC: O(1)
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        n= len(nums)
        if n <=4:
            return 0
        
        # print(nums)
        ans= float("inf")
        
        for i in range(4):
            j= n- 4+ i
            ans = min(ans, nums[j]- nums[i])
            
        return ans
