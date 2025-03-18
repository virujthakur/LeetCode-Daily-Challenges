class Solution:
    #TC: O(N* LOG(32)* 32) SC: O(N* 32)
    def longestNiceSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        prefix_bitmap = [[0]* (n+1) for _ in range(32)]

        for j in range(32):
            for i in range(n):
                if 1<<j & nums[i]:
                    prefix_bitmap[j][i+1] = prefix_bitmap[j][i]+1
                else:
                    prefix_bitmap[j][i+1] = prefix_bitmap[j][i]

        # print(prefix_bitmap)
        for l in range(n):
            r = n+1
            for j in range(32):
                newr = bisect.bisect_left(prefix_bitmap[j], prefix_bitmap[j][l]+2, l+1, n+1)
                r= min(newr, r)

            # print(l, r)
            ans = max(r-l-1, ans)

        return ans

