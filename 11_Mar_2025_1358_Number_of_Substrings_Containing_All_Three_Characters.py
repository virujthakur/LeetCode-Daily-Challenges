class Solution:
    #TC: O(NLOGN) SC: O(N)
    def numberOfSubstrings(self, s: str) -> int:
        n= len(s)
        prefix = defaultdict(list)
        for c in ['a', 'b', 'c']:
            prefix[c] = [0]* (n+1)

        for i,c1 in enumerate(s):
            for c2 in ['a', 'b', 'c']:
                if c1 == c2:
                    prefix[c2][i+1] = prefix[c2][i] + 1
                else:
                    prefix[c2][i+1] = prefix[c2][i]

        ans = 0

        for i, c1 in enumerate(s):
            r = -1
            for c2 in ['a', 'b' ,'c']:
                r= max(r, bisect.bisect_left(prefix[c2], prefix[c2][i]+1, i, n+1))
            
            ans += n+1-r

        return ans
