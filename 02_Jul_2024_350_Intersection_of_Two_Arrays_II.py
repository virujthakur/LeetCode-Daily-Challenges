class Solution:
    #TC: O(N) SC: O(N)
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        f1= Counter(nums1)
        f2= Counter(nums2)
        
        vis = set()
        ans = []
        for num in nums1:
            if num not in vis and num in f2:
                a = [num]* min(f1[num], f2[num])
                ans+= a
                vis.add(num)
                
        for num in nums2:
            if num not in vis and num in f1:
                a = [num]* min(f1[num], f2[num])
                ans+= a
                vis.add(num)
                
        return ans
