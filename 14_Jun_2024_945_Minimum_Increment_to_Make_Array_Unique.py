class Solution:
    #TC: O(NLOGN) SC: O(1)
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        n= len(nums)
        ans = 0
        
        for i in range(1, n):
            if nums[i] <= nums[i-1]:
                diff = nums[i-1]- nums[i] + 1
                ans+= diff
                nums[i] = nums[i-1] + 1
                
        return ans
                
            
            
        
        
