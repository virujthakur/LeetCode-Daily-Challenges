class Solution:
    # TC: O(T*26 + N) SC: O(26)
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        mod = 10**9 + 7
        f = [0] * 26
        for c in s:
            f[ord(c)- ord('a')] +=1

        for i in range(t):
            newf = [0]* 26
            for i in range(26):
                if i == 25:
                    newf[0] += f[i]
                    newf[1] += f[i]
                else:
                    newf[i+1] += f[i]

            f = newf

        ans = 0
        # print(newf)
        for i in range(26):
            ans += f[i]
            ans %= mod

        return ans
