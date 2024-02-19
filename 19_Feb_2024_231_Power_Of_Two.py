class Solution:
    #TC: O(1) SC: O(1)
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and not (n & (n-1))
