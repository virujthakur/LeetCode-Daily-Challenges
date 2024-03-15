class Solution:
    # TC: O(N) SC: O(N)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        n= len(nums)   
        ans= [1]* n
        pref = [1]* n
        suff = [1]* n
        for i in range(n):
            prod*= nums[i]
            pref[i]= prod
            
        prod =1
        for i in range(n):
            prod *= nums[n-1-i]
            suff[n-1-i]= prod
        
        for i in range(n):
            if i-1 >=0:
                ans[i]*= pref[i-1]
            if i+1 < n:
                ans[i]*= suff[i+1]
                
        return ans
