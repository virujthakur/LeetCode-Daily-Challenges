class Solution:
        #TC : O(NLOGN) SC: O(1)
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        l= sorted(list(set(nums1) & set(nums2)))
        return l[0] if l else -1
        
