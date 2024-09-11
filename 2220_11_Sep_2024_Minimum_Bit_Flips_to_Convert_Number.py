class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        return str(bin(start^goal)).count('1')
