class Solution:
    #TC: O(N) SC: O(1)
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        n= len(nums)
        mn= 10**9
        res = 0
        count = 0
        
        for num in nums:
            res += max(num, num^ k)
            
            if (num^k) > num:
                count+=1
            
            mn= min(mn, abs(num- (num^k)))
            
        if count%2:
            return res - mn
        else:
            return res
