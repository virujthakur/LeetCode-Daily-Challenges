class Solution:
    #TC: O(N) SC: O(N)
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        ans = 0
        n = len(differences)
        prefix = [0]* n
        s = 0
        for i in range(n):
            s+= differences[i]
            prefix[i] = s

        mx, mn = max(prefix), min(prefix)

        for i in range(lower, upper+1):
            start = i
            if lower<= start+ mx <= upper and lower <= start+ mn <= upper:
                ans+=1

        return ans
