class Solution:
    # TC: O(N) SC: O(N)
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n= len(nums)
        prefix = [0]* n
        suffix = [0]* n
        
        s = 0
        for i in range (n):
            s += nums[i]
            prefix[i]= s
        
        s = 0
        for i in range (n):
            s+= nums[-1-i]
            suffix[-1-i]= s
        
        # print(prefix)
        # print(suffix)
            
        res= [0]* n
        for i in range(n):
            if i-1 >= 0:
                res[i]+= (nums[i]* i)- prefix[i-1]
            if i+1< n:
                res[i]+= suffix[i+1] - (nums[i]* (n-i-1)) 
        
        return res
