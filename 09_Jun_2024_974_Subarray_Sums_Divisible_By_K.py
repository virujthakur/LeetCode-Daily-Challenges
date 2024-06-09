class Solution:
    #TC: O(N) SC: O(N)
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        f = defaultdict(int)
        ans = 0
        s = 0
        f[0] = 1
        for num in nums:
            s+= num
            rem= s%k
            if rem in f:
                ans+= f[rem]
                
            f[rem]+=1
            
        return ans
