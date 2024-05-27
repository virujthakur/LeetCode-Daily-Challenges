class Solution:
    #TC: O(NLOGN) SC: O(1)
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        mx= max(nums)
        
        for i in range(1, len(nums)+1):
            r= bisect.bisect_left(nums, i, 0, len(nums))
            count = len(nums)-r
            if count == i:
                return i
            
        return -1
            
