class Solution:
    #TC: O(N) SC: O(1)
    def findMaxK(self, nums: List[int]) -> int:
        ans = -1
        s= set()
        for num in nums:
            if -num in s:
                ans= max(ans, abs(num))
            s.add(num)
            
        return ans
