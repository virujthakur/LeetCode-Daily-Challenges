class Solution:
    #TC: O(N^2) SC:O(1)
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n= len(nums)
        
        dp = defaultdict(int)
        ans=0
        for i in range(1, n):
            for j in range(i):
                cnt=0
                if (j, nums[i]- nums[j]) in dp:
                    cnt = dp[(j, nums[i]- nums[j])]
                
                dp[(i, nums[i]- nums[j])] += cnt+1
                ans+= cnt
        
        return ans
        
                
