class Solution:
    #TC: O(32) SC: O(1)
    def findComplement(self, num: int) -> int:
        var = ((1<<(len(bin(num))-2)) - 1)
        return num ^ var
