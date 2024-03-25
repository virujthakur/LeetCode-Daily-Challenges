class Solution:
    #TC: O(N) SC: O(1)
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n= len(nums)
            
        for i in range(n):
            nums[abs(nums[i])-1]*=-1
        
        s= []
        for i in range(n):
            if nums[abs(nums[i])-1]> 0:
                s.append(abs(nums[i]))
            nums[abs(nums[i])-1]*=-1
                
        return s
