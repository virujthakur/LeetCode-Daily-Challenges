class Solution:
    #TC: O(N) SC: O(N)
    def minOperations(self, nums: List[int], k: int) -> int:
        if k > min(nums):
            return -1
        elif k == min(nums):
            return len(set(nums)) -1
        else:
            return len(set(nums))
