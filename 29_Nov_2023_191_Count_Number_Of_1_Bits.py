class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        for i in range(32):
            if n & 1:
                ans+=1
            n >>= 1
        return ans
