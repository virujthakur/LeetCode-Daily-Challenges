class Solution:
    #TC: O(2^N + SORT) SC: O(1)
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        n= len(nums)
        nums.sort()
        
        def isValid(idx, curMask):
            for i in range(n):
                if (1<<i)& curMask:
                    if(nums[idx]- nums[i]== k):
                        return False
            return True
            
        ans = 0
        def recur(idx, curMask):
            nonlocal ans
            if idx == n:
                ans+=1
                return
              
            if isValid(idx, curMask):
                recur(idx+1, curMask | (1<<idx))
            recur(idx+1, curMask)
          
        recur(0, 0)
        return ans-1
                        
            
