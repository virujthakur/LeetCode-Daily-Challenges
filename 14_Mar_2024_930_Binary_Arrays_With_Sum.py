class Solution:
    #TC: O(N) SC: O(1)
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        f= defaultdict(int)
        f[0]=1
        s= 0
        ans= 0
        for num in nums:
            s+= num
            ans+= f[s-goal]
            f[s]+=1
            
        return ans
