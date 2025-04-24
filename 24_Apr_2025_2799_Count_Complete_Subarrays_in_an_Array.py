class Solution:
    #TC: O(N^2) SC: O(N)
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        complete = set(nums)
        ans = 0
        for i in range(n):
            subset = set()
            for j in range(i, n):
                subset.add(nums[j])
                if len(subset) == len(complete):
                    ans+=1

        return ans


        
