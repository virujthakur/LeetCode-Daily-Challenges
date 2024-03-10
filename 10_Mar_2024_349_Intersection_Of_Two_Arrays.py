class Solution:
    #TC : O(N) SC: O(N)
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))
