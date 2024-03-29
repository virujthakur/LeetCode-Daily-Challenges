class Solution:
    #TC: O(N) SC: O(1)
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n= len(nums)
        mx= max(nums)
        i,j= 0,0
        f=0
        ans= 0
        
        while j<n:
            while j<n and f<k:
                if nums[j]== mx:
                    f+=1
                j+=1
            
            if f==k:
                ans+= n-j+1
            
            while i<j and f>=k:
                if nums[i]== mx:
                    f-=1
                
                if f==k:
                    ans+= n-j+1
                i+=1
                
        return ans
