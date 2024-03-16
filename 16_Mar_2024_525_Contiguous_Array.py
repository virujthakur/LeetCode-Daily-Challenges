class Solution:
    #TC: O(N) SC: O(N)
    def findMaxLength(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if not nums[i]:
                nums[i] = -1
        
        # print(nums)
        f= {}
        s, ans = 0, 0
        f[0] = -1
        for i,num in enumerate(nums):
            s+= num
            
            if s in f:
                ans= max(ans, i- f[s])
                f[s]= min(f[s], i)
            else:
                f[s]= i
        
        return ans
