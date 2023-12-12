class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n= len(nums)
        myNums= [num-1 for (num) in nums]
        
        prod= 0
        for i in range (n):
            for j in range (i+1, n):
                prod= max(prod, myNums[i]* myNums[j])
                
        return prod
        
