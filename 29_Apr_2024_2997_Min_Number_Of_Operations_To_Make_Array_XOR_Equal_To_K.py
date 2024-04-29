class Solution:
    # TC: O(N) SC: O(1)
    def minOperations(self, nums: List[int], k: int) -> int:
        n= len(nums)
        
        bitCount= [0]* 32
        for num in nums:
            for i in range(32):
                if (1<<i) & num:
                    bitCount[i]+=1
                    
        bitCountK= [0]* 32
        
        for i in range(32):
            if (1<<i) & k :
                bitCountK[i]+=1
                
        ops= 0
        for i in range(32):
            if bitCount[i]% 2!= bitCountK[i]% 2:
                ops+=1
                
        return ops
