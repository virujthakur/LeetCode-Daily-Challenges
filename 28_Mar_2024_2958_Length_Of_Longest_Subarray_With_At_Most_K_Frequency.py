class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n= len(nums)
        # TC: O(N) SC: O(1)
        f= defaultdict(int)
        i,j= 0, 0
        res= 0
        while j<n:
            
            while j<n:
                f[nums[j]]+=1
                if f[nums[j]] > k:
                    j+=1
                    break
                j+=1
            
            if f[nums[j-1]] <= k:
                res= max(res, j-i)
            else:
                res= max(res, j-i-1)
            # print(i,j,res)
            
            while i<j and f[nums[j-1]]> k:
                f[nums[i]]-=1
                i+=1
                
        
        return res
