class Solution:
    #TC: O(2^N)* N SC: O(1)
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n= len(nums)
        cnt = 0
        ansSum = 0
        
        for i in range(1<<n):
            orSum = 0
            for j in range(n):
                if (i & (1<<j)):
                    orSum |= nums[j]
                    
            if ansSum < orSum:
                ansSum = orSum
                cnt =1
            elif ansSum == orSum:
                cnt+=1
            
            # print(orSum)
                    
        return cnt
