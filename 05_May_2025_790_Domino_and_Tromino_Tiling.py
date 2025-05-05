class Solution:
    def numTilings(self, n: int) -> int:
        mod = 10**9+7
        @cache
        def recur(i , gap):
            if i == n and not gap:
                return 1
            if i >= n:
                return 0

            ans = 0
            if gap:
                ans+= recur(i+1, False) % mod + recur(i+1, True) % mod
            else:
                ans+= recur(i+1, False) % mod + recur(i+2, False) % mod + 2* recur(i+2, True) % mod

            return ans

        return recur(0, False) % mod
