class Solution:
    # TC: O(M* N^2) SC: O(1)
    def isAP(self, nums) :
        n= len(nums)
        if n == 1:
            return True
        d= nums[1]- nums[0]
        for i in range (2, n):
            if nums[i]- nums[i-1] != d :
                return False
        
        return True        
    
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        n= len(nums)
        m= len(l)
        ans= []
        for i in range (m):
            left = l[i]
            right = r[i]
            
            temp= nums[l[i]: r[i]+1]
            temp.sort()
            ans.append(self.isAP(temp))
        
        return ans
