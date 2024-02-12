class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #TC: O(N) SC: O(1)
        return Counter(nums).most_common()[0][0]
