class Solution:
    #TC: O(N) SC: O(1)
    def buildArray(self, nums: List[int]) -> List[int]:
        return [nums[num] for num in nums]
