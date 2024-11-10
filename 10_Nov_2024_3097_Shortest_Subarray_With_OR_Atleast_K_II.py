class Solution: 
    #TC: O(32* 2(N)) SC: O(32)
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        orSum = 0
        bitCnt = [0]* 32
        ans = n+1
        i = 0
        
        for j in range(n):
            orSum |= nums[j]
            
            for _k in range(32):
                if (1<<_k) & nums[j]:
                    bitCnt[_k]+=1
            
            # print(orSum)
            while i<=j and orSum >= k:
                
                # print(i, j)
                ans = min(ans, j-i+1)
                
                for _k in range(32):
                    if (1<<_k) & nums[i]:
                        bitCnt[_k]-=1
                        
                        if bitCnt[_k] == 0:
                            orSum -= (1<<_k)
                
                i+=1
                
        return ans if ans < n+1 else -1
