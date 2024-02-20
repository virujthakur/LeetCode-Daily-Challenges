class Solution:
    #TC: O(N) SC: O(1)
    def missingNumber(self, nums: List[int]) -> int:
        n= len(nums)
        nums= [num+1 for num in nums]
        # print(nums)
        for i in range(n):
            if abs(nums[i]) < n+1:
                nums[abs(nums[i])-1] = -nums[abs(nums[i])-1]
                # print(nums)
        
        # print(nums)
        for i in range(n):
            if nums[i] >=0:
                return i
        
        
        return n
