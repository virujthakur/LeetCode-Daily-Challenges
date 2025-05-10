class Solution:
    #TC: O(N) SC: O(1)
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        s1, s2 = sum(nums1), sum(nums2)
        c1, c2 = nums1.count(0), nums2.count(0)

        if s1 + c1 > s2+ c2:
            if c2 == 0:
                return -1
        
        if s2 + c2 > s1+ c1:
            if c1 == 0:
                return -1

        return max(s1+c1, s2+ c2)
