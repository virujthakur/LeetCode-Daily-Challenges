class Solution:
    #TC: O(N) SC: O(N)
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n= len(nums)
        for i,num in enumerate(nums):
            nums[i] = nums[i]%2
            
        # print(nums)
        f= defaultdict(int)
        s = 0
        ans = 0
        f[0]= 1
        
        for num in nums:
            s+= num
            ans+= f[s-k]
            f[s]+=1
            
        return ans
        
