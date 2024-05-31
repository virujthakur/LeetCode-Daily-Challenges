class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        #TC: O(N) SC: O(1)
        n= len(nums)
        xorSum = 0
        for num in nums:
            xorSum^= num
            
        x,y = 0, 0
        rsbm = xorSum & (-xorSum)
        for num in nums:
            if (num& rsbm) == 0:
                x ^= num
            else:
                y^= num
                
        return [x,y]
        
