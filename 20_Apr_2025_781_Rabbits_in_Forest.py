class Solution:
    # TC: O(N) SC: O(N)
    def numRabbits(self, answers: List[int]) -> int:
        f= defaultdict(int)
        for a in answers:
            f[a]+=1

        ans = 0
        for (k,v) in f.items():
            ans += int(ceil(v / (k+1))) * (k+1)

        return ans
