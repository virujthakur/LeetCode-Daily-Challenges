class Solution:
    #TC: O(2^N)*N SC: O(1)
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n= len(nums)
        ans = []
        for i in range((1<<n)):
            subset = []
            for j in range(n):
                if (1<<j) & i:
                    subset.append(nums[j])
                    
            ans.append(subset)
            
        return ans
        
