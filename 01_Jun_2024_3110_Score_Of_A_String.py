class Solution:
    #TC: O(N) SC: O(1)
    def scoreOfString(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(1, n):
            ans += abs(ord(s[i]) - ord(s[i-1]))
            
        return ans
