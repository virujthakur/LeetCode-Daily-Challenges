class Solution:
    #TC: O(N^2) SC: O(1)
    def frequencySort(self, nums: List[int]) -> List[int]:
        return sorted(nums, key= lambda x: (Counter(nums)[x], -x))

        
