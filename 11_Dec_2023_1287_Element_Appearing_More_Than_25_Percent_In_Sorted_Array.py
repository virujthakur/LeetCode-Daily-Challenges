class Solution:
    # TC: O(N^2) SC: O(1)
    def findSpecialInteger(self, arr: List[int]) -> int:
        n= len(arr)
        for i in set(arr):
            if 4 * arr.count(i) > n:
                return i
        return -1
