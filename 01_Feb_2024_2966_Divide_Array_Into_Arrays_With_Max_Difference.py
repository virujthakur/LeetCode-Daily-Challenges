import bisect
class Solution:
    #TC: O(N) SC: O(1)
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        
        n= len(nums)
        i= 0
        ans = []
        while i < n:
            j = bisect.bisect(nums, nums[i] + k, i, len(nums))
            if j-i < 3 :
                return []
            else :
                ans.append(nums[i: i+3])
                i+= 3
                
        return ans
