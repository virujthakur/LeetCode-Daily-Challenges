class Solution:
    #TC: O(N) SC: O(N)
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        n = len(dominoes)
        for d in dominoes:
            d[0] , d[1] = min(d[0],d[1]), max(d[0], d[1])

        f = defaultdict(int)
        for d in dominoes:
            f[tuple(d)]+=1

        ans = 0
        for (k,v) in f.items():
            ans += v * (v-1) // 2

        return ans
