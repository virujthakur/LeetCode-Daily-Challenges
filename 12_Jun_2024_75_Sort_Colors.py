class Solution:
    #TC: O(N) SC O(1)
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i= 0
        j= 0
        k= len(nums)-1
        
        while j<= k:
            if nums[j]== 0:
                nums[j], nums[i]= nums[i], nums[j]
                i+=1
            
            elif nums[j]==2:
                nums[j], nums[k]= nums[k], nums[j]
                k-=1
                
                if nums[j]==0 or nums[j]==2:
                    j-=1
            
            j+=1
            
        
