class Solution:
    #TC: O(LOGN) SC: O(1)
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)
        neg = bisect.bisect_left(nums, 0, 0, len(nums))
        pos = bisect.bisect_right(nums, 0, 0, len(nums))
        return max(neg, n-pos)


        
