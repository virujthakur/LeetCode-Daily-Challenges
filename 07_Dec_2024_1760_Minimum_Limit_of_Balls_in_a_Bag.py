class Solution:
    #TC: O(NLOGN) SC: O(1)
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        nums.sort()
        l =1
        h = max(nums)
        ans = h
        
        def isValid(mid):
            cnt = 0
            
            for num in nums:
                cnt += (num // mid) - 1 if num % mid == 0 else (num // mid)
                
            return cnt <= maxOperations
        
        while l<=h:
            mid = (l+h)//2
            if isValid(mid):
                ans = min(ans, mid)
                h= mid-1
            else:
                l= mid+1
                
        return ans
                
