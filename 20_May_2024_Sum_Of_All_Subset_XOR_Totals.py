class Solution:
    #TC: O(2^N) SC: O(1)
    def subsetXORSum(self, nums: List[int]) -> int:
        n= len(nums)
        res = 0
        
        for i in range((1<<n)):
            ans = 0
            for j in range(n):
                if (1<<j)& i:
                    ans^= nums[j]
                    
            res+= ans
            
        return res
                    
        
