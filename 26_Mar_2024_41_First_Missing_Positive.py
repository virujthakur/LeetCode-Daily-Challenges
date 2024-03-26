class Solution:
    #TC: O(N) SC: O(1)
    def firstMissingPositive(self, nums: List[int]) -> int:
        n= len(nums)
        for i in range(n):
            if nums[i]<=0 :
                nums[i]= n+1
        
        for i in range(n):
            v= abs(nums[i])
            if v>0 and v<=n:
                if nums[v-1]<0:
                    continue
                nums[v-1]*= -1
        
        for i in range(n):
            if nums[i]> 0:
                return i+1
            
        return n+1
