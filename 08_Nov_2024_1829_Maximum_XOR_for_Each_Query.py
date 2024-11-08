class Solution:
    #TC: O(N* maximumBit) SC: O(maximumBit)
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        n = len(nums)
        
        bitCnt = [0 for _ in range(maximumBit)]
        
        for i in range(maximumBit):
            cnt = 0
            for j in range(n):
                if (1<<i) & nums[j]:
                    cnt+=1
                    
                bitCnt[i] = cnt
            
        res = []
        
        
        for i in range(n):
            ans = 0
            for j in range(maximumBit):
                if bitCnt[j] % 2:
                    continue
                else:
                    ans |= (1<< j)
                    
            for j in range(maximumBit):
                if nums[n-1-i] & (1<<j):
                    bitCnt[j] -=1
                    
            res.append(ans)
            
        return res
            
                    
