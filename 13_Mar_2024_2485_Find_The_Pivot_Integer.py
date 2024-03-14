# TC:O(1) SC: O(1)
class Solution:
    def pivotInteger(self, n: int) -> int:
        return int(sqrt((n + n**2)/2)) if sqrt((n + n**2)/2).is_integer() else -1
